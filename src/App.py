#import the libraries
import pandas as pd
import numpy as np
import streamlit as st
import os
import time

try:
    #insert headers
    st.header(" Welcome to Sales Prediction Using Prophet ")
    st.subheader("To help you know your future sales📈...")
    st.image("src/images/future.PNG")
    #Take input
    with st.form("This form",clear_on_submit = True):
        st.subheader("Enter the number of days you want to predict, And the frequency as D for Daily or W for weekly ")
        Number_of_days=st.number_input("number of days")
        frequency=st.text_input("Frequency 'D' for Daily 'W' for weekly ")
        submit = st.form_submit_button("Predict your sales")
    #process the input

        print(f"[INFO]: Inputs received")
        if submit:
            st.success("Inputs received successfully ",icon="✅")
        
        #show progress
            with st.spinner("Prediction in progress..."):
                time.sleep(10)


   

    #import model

    #pass inputs to the model

    #show results
    
except:
    st.error("something went wrong")