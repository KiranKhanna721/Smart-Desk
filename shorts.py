import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

import cohere
co = cohere.Client('nE237kNXwduF9qeMaou4mGXzbfMmnrfWgiECpDHq')


def app():
    st.title("Short Essay")
    text = st.text_input("Topic")
    submit = st.button('Submit')
    if submit:
        if text!=None:
            response = co.generate(model='xlarge',
                                   prompt='Topic:Importance of Education in Life\n\nEssay:First of all, Education teaches the ability to read and write. Reading and writing is the first step in Education. Most information is done by writing. Hence, the lack of writing skill means missing out on a lot of information. Consequently, Education makes people literate. Education is extremely important for employment. It certainly is a great opportunity to make a decent living. This is due to the skills of a high paying job that Education provides. Uneducated people are probably at a huge disadvantage when it comes to jobs. It seems like many poor people improve their lives with the help of Education.\n--\nTopic:Familiarity between Technology and Science\n\nEssay:As they are completely different fields but they are interdependent on each other. Also, it is due to science contribution we can create new innovation and build new technological tools. Apart from that, the research conducted in laboratories contributes a lot to the development of technologies. On the other hand, technology extends the agenda of science.\n--\nTopic:'+str(text)+'\n\nEssay:',
                                   max_tokens=200,
                                   temperature=0.8,
                                   k=0,
                                   p=1,
                                   frequency_penalty=0,
                                   presence_penalty=0,
                                   stop_sequences=["--"],
                                   return_likelihoods='NONE')
            print('Prediction: {}'.format(response.generations[0].text))
            st.write(response.generations[0].text)
            