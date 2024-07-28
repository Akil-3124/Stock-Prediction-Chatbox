import streamlit as st
import pandas as pd
import requests
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq  
import streamlit.components.v1 as com
import fetch_data
from openai import OpenAI


def app():

    # Chat Section
    st.title("Stock Market Chat Assistant")
    com.iframe("https://lottie.host/embed/fcd1a67a-214a-41e0-bce0-04acc5938708/L5n6eH0xdv.json")
    st.write("Welcome to our AI Stock Prediction Chatbox! Harness the power of advanced artificial intelligence to make informed investment decisions with real-time stock price forecasts, personalized insights, and comprehensive historical data analysis. Our chatbox also provides market sentiment analysis, helping you stay ahead of trends and make strategic investments based on the latest market data and news.")
    
    @st.cache_data
    def fetch_data(query):
        API_ENDPOINT = "https://stock.coralflow.co/stock"

        headers = {
            "name": query,
            "Authorization": "Bearer api key" 
        }

        response = requests.request("GET", API_ENDPOINT, headers=headers)
        return response.json()
        
    # Initialize OpenAI client
    @st.cache_data
    def ai_chat(system_content, user_query, news_content, price_content, risk_content):
        client = OpenAI(
            base_url='http://api.coralflow.co/v1',
            api_key='api key')

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content":news_content},
                {"role": "system", "content":price_content},
                {"role": "system", "content":risk_content},
                {"role": "system", "content":system_content},
                {"role": "user", "content": user_query}
            ]
        )

        message = completion.choices[0].message
        # Assuming message is an instance of ChatCompletionMessage
        return message.content



    # User input for the combined query
    user_query = st.text_input("Enter your query")

    if user_query:
        # Fetch stock data and use it as system content for the AI chat
        stock_data = fetch_data(user_query)
        system_content = f"Here is the stock data: {stock_data}. Now, answer the following question:"

        recent_news=fetch_data(user_query).get("recentNews", [])
        news_content= f"Here is the stock data: {recent_news}. Now, answer the following question:"

        risk_meter =fetch_data(user_query).get("riskMeter", [])
        risk_content= f"Here is the stock data: {risk_meter}. Now, answer the following question:"

        current_price= fetch_data(user_query).get("currentPrice", {})
        price_nse = current_price.get('NSE', 'N/A')
        price_bse = current_price.get('BSE', 'N/A')
        price_content= f"Here is the stock data: {price_bse,price_nse}. Now, answer the following question:"

        # Get AI response
        ai_response = ai_chat(system_content, user_query, news_content,price_content,risk_content)
        
        # Display only the AI chat response
        st.subheader("AI Chat Response")
        st.write(ai_response)