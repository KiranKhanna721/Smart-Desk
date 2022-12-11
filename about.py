import pandas as pd
import numpy as np
import streamlit as st
import wikipedia

def app():
    st.title("About a Company")
    #st.image("https://image.shutterstock.com/image-vector/cute-chatbot-robot-assistant-different-600w-1984034186.jpg")
    text = st.text_input("Company Name in lower case")
    submit = st.button('Submit')
    if submit:
        if text!=None:
            tex = str(text) + " company"
            t = wikipedia.summary(tex, sentences=5)
            st.write(t)
            l = wikipedia.page(tex).images
            if len(l)!=0:
                ab=[]
                for i in l:
                    k=i.find("logo")
                    k1 = i.find('.png')
                    k2=  i.find(".jpg")
                    if(k!=-1):
                        if(k1!=-1 or k2!=-1):
                            ab.append(i)
                if len(ab)!=0:
                    st.image(ab[-1])