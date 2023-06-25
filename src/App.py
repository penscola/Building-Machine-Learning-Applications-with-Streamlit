import pandas as pd
import numpy as np
import streamlit as st
import os
import time
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pip


try:
    #insert headers
    st.header(" Welcome to Sales Prediction Using Prophet ")
    st.subheader("To help you know your future sales📈...")
    st.image("./images/future.png", width=500, caption="Sales Prediction")

    Disp_results = pd.DataFrame()  # Initialize for download

    # Take input
    with st.form("This form", clear_on_submit=True):
        st.subheader("Enter the number of day(s)/Week(s) you want to predict, And the frequency as D for Daily or W for weekly ")

        frequency = str(st.text_input("Frequency 'D' for Daily 'W' for weekly ")).upper()  # convert to string and change to upper

        Number_of_days = int(st.number_input("Number of day(s)/Week(s)"))  # convert to int

        submit = st.form_submit_button("Predict your sales")

        # process the input
        if submit:
            # check if we have the right data type
            if frequency == "D" or frequency == 'W':
                st.success("Inputs received successfully ✅")

                # import model
                with open('./model/prophet_model.pkl', 'rb') as f:
                    model = pickle.load(f)

                # pass inputs to the model(To make predictions, prophet requires number of days and frequency)
                future = model.make_future_dataframe(periods=Number_of_days, freq=str(frequency), include_history=False)

                # Make prediction
                forecast = model.predict(future)

                # show results
                print(f'[INFO]: The whole results {forecast}')

                # pick the relevant columns from the forecast
                sales_forecast = forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']]

                # rename the columns
                Disp_results = sales_forecast.rename(columns={'ds': 'Date', 'yhat_lower': 'lowest Expected sales', 'yhat_upper': 'Highest Expected Sales', 'yhat': 'Expected Sales'})

                # print result dataframe to terminal
                print(f'[INFO]: results dataframe {Disp_results}')

                # show progress
                with st.spinner("Prediction in progress..."):
                    time.sleep(2)
                    st.balloons()
                    st.success("Great✅")

                # Display results
                if frequency == "W":
                    output_frequency = 'Week(s)'
                else:
                    output_frequency = 'Day(s)'

                # Check frequency
                st.write(f"These are your predicted sales in the next {Number_of_days} {output_frequency}")
                st.dataframe(Disp_results)

                # Display the graph of sales
                st.title(f"Line Graph Of Predicted Sales Over {Number_of_days} {output_frequency} ")
                # Line Graph
                st.line_chart(data=Disp_results, x='Date', y='Expected Sales')
                print('[INFO]: Line Chart displayed')

            else:
                st.error("Input the right frequency or Days ⚠")

        # Print input to the terminal
        print(f'[INFO]: These are the inputs to the model {Number_of_days},{frequency}')
        print(f"[INFO]: Inputs received")


    # Create a function to convert df to csv
    def convert_to_csv(df):
        return df.to_csv()


    # Create an expander
    expand = st.expander('Download Results as CSV')
    with expand:
        st.download_button(
            'Download results',
            convert_to_csv(Disp_results),
            'prediction_results.csv',
            'text/csv',
            'download'
        )


    # Create Sidebar for Description
    sidebar = st.sidebar.title('Sales Prediction')

    # first option
    option1 = st.sidebar.button('About', key="About")

    # second option
    option2 = st.sidebar.button('About the sales prediction', key="sales prediction")

    # Display text for a selected option
    if option1:
        st.sidebar.write('This is a Sales prediction app Using Prophet(Developed by meta), this project was done under the Azubi Africa Data Analysis Training program ')

    elif option2:
        st.sidebar.write('This is a time series analysis & forecasting problem. In this project, we shalll predict store sales on data from Corporation Favorita, a large Ecuadorian-based grocery retailer. Specifically, this app predicts the sales for up to  weeks in advance for Corporation Favorita ')

except:
    st.error('''something went wrong: Make sure you entered the correct number of days
    otherwise contact admin!
    '''
             )
 