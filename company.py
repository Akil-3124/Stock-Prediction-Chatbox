import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import yfinance as yf
from datetime import date
import requests
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq  
import altair as alt
import streamlit.components.v1 as com
import fetch_data

def app():

    st.title("Company Profile")
    com.iframe("https://lottie.host/embed/a6bc6e55-50a8-424d-9b25-47b28ef39b9f/Fr6x3tlTj1.json")
    st.write("Welcome to our AI Company Profile Chatbox! Explore detailed company profiles with our advanced AI-driven platform. Access real-time data, financial metrics, and key performance indicators to make informed investment decisions. Our chatbox provides comprehensive analysis, including historical performance, market trends, and industry comparisons, helping you gain a deep understanding of companies and make strategic investments based on the most current and relevant information.")
    
    # User Input for Stock Name
    stock_name = st.text_input("Enter Stock Name",)

    # Fetch data if user enters a stock name
    if stock_name:
        data = fetch_data.get_recent_news(stock_name)
        
        # Display company name, industry, current price, and risk meter
        st.subheader("Stock Information")
        st.write(f"Company Name: {data['companyName']}")
        st.write(f"Industry: {data['industry']}")
        st.write(f"Current Price: ${data['currentPrice']}")
        st.write(f"Risk Meter: {data['riskMeter']}")
        
        # Display company description if available
        if 'companyProfile' in data and 'companyDescription' in data['companyProfile']:
            st.subheader("Company Description")
            st.write(data['companyProfile']['companyDescription'])
        else:
            st.info("Company description not available.")