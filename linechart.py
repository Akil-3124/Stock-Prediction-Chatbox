import requests
import streamlit as st
import pandas as pd
import altair as alt
import streamlit.components.v1 as com
import fetch_data

def app():
    st.title("Current price of stock")
    com.iframe("https://lottie.host/embed/6fcfbac6-1106-46aa-a2c9-2383a60d115a/O7nus3XPeL.json")
    st.write("Welcome to our AI Stock Price Chatbox! Instantly access the latest stock prices with our advanced AI-driven platform. Get real-time updates, personalized insights, and comprehensive historical data analysis to make informed investment decisions. Our chatbox also provides market sentiment analysis, helping you stay ahead of trends and make strategic investments based on the most current market data and news.")
    
    name = st.text_input("Enter stock name 1")
    name1 = st.text_input("Enter stock name 2")
    name2 = st.text_input("Enter stock name 3")

    if name and name1 and name2:
        news_results1 = fetch_data.get_recent_news(name).get('currentPrice', {})
        news_results2 = fetch_data.get_recent_news(name1).get('currentPrice', {})
        news_results3 = fetch_data.get_recent_news(name2).get('currentPrice', {})

        price1 = news_results1.get('NSE', 'N/A')
        price2 = news_results2.get('NSE', 'N/A')
        price3 = news_results3.get('NSE', 'N/A')

        st.write(f"Current price of {name}: {price1}")
        st.write(f"Current price of {name1}: {price2}")
        st.write(f"Current price of {name2}: {price3}")

        data = {
                'Stock': [name, name1, name2],
                'Price': [price1, price2, price3]
            }

        df = pd.DataFrame(data)

        bar_chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('Stock', axis=alt.Axis(labelAngle=0)),
                y=alt.Y('Price', scale=alt.Scale(domain=[0, max(df['Price'])])),
                color='Stock'
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                grid=True
            ).configure_view(
                strokeWidth=0
            )

        st.altair_chart(bar_chart, use_container_width=True)