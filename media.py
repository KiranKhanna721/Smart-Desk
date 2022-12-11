import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from expertai.nlapi.cloud.client import ExpertAiClient
import os
import tweepy
import re
import emoji
import nltk
nltk.download('words')

#Tweets
my_bearer_token = "AAAAAAAAAAAAAAAAAAAAADnKawEAAAAArzcTtXJOw1Jx05SYlL%2F4J5%2F6Zv0%3Die1sm7TPVHtksmylWglnbmKUVNVzf7cEYBzeHDjTvB9aUggCQT"
cli = tweepy.Client(bearer_token=my_bearer_token)

def cleaner(tweet):
    words = set(nltk.corpus.words.words())
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.distinct_emoji_list(c)) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet  = tweet.replace("\n"," ")
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet)
                     if w.lower() in words or not w.isalpha())
    return tweet

os.environ["EAI_USERNAME"] = 'khkiran01@gmail.com'
os.environ["EAI_PASSWORD"] = 'Meera@1977'
client = ExpertAiClient()
def sentiment_overall(client, text):
    try:
        input_text = str(text)[0:10000]  # limit the input size
        document = client.specific_resource_analysis(
        body={"document": {"text": input_text}}, 
        params={'language': 'en', 'resource': 'sentiment'
       })
        return document.sentiment.overall
    except Exception as e: 
        print(str(e) +": " + str(text))

def percentage(part,whole):
    return 100 * float(part)/float(whole)

def hate_speech(client,text):
    detector = 'hate-speech'
    language= 'en'
    output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})
    for category in output.categories:
        return category.hierarchy

def emotion(client,text):
    taxonomy = 'emotional-traits'
    language= 'en'
    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})
    for category in output.categories:
        return category.hierarchy


def app():
    text = st.text_input("Company Name in lower case")
    st.write("If tweets are none , trying writing full name of the company or adding company word at ending")
    submit = st.button('Submit')
    if submit:
        if text!=None:
            tw = str(text)
            response = cli.search_recent_tweets(tw,max_results=60)
            tweets = response.data
            total = len(tweets)
            if len(tweets)!=0:
                tweets_texts = []
                for tweet in tweets:
                    tweets_texts.append(tweet.text)
                df = pd.DataFrame(data =  tweets_texts, columns=["Tweets"])
                st.header("The Top 60 Tweets")
                st.write(df)
                df['text'] = df['Tweets'].map(lambda x: cleaner(x))
                df['overall'] = df['text'].apply(lambda text: sentiment_overall(client,text))
                df['overall_score'] = df['overall'].apply(lambda c: 'pos' if c >=0 else 'neg')
                p=0
                ne=0
                for n in df['overall_score']:
                    if n =='pos':
                        p+=1
                    else:
                        ne+=1
                positive = percentage(p, total)
                negative = percentage(ne,total)
                positive = format(positive, '.1f')
                negative = format(negative, '.1f')
                st.header("Sentiment Analysis Of Tweets")
                labels = ['Positive ['+str(positive)+'%]' ,'Negative ['+str(negative)+'%]']
                sizes = [positive,negative]
                colors = ['yellowgreen','red']
                patches, texts = plt.pie(sizes,colors=colors, startangle=90)
                plt.style.use('default')
                plt.legend(labels)
                plt.title("Sentiment Analysis Result for = "+text+"" )
                plt.axis("equal")
                plt.savefig('my_plot.png')
                st.image('my_plot.png')
                # hate speech
                st.header("Hate Speech Detection")
                df['hatespeech'] = df['text'].apply(lambda text: hate_speech(client,text))
                a=[]
                for h in df['hatespeech']:
                    if h!=None:
                        a.append(h)
                if len(a)==0:
                    st.subheader("No Hate Speech Detected In Tweets")
                else:
                    st.subheader("Hate Speech Detected in Tweets")
                    st.write(a)

                # Emotional
                st.header("Emotional traits")
                df['emotional'] = df['text'].apply(lambda text: emotion(client,text))
                b=[]
                for e in df['emotional']:
                    if e!=None:
                        b.append(e)
                if len(b)==0:
                    st.subheader("No Emotional traits")
                else:
                    st.subheader("Emotional traits")
                    st.write(b)