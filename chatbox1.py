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

    # Function to fetch stock data
    def get_stock_data(symbol, start, end):
        return yf.download(symbol, start=start, end=end)


    def get_sentiment_data(symbol, start, end):
        analyzer = SentimentIntensityAnalyzer()
        dummy_data = pd.date_range(start=start, end=end, freq='D')
        sentiment_scores = [analyzer.polarity_scores("This is a placeholder text for sentiment analysis.")["compound"] for _ in dummy_data]
        sentiment_df = pd.DataFrame({'Date': dummy_data, 'Sentiment': sentiment_scores})
        sentiment_df.set_index('Date', inplace=True)
        return sentiment_df

    # Function to prepare data for prediction
    def prepare_data(data, sentiment_data):
        data = data.join(sentiment_data, how='left').fillna(0)  # Join sentiment data and fill missing values with 0
        data['Date'] = data.index
        data['Date'] = pd.to_numeric(data['Date'].apply(lambda x: x.toordinal()))
        X = data[['Date', 'Sentiment']]
        y = data['Close']
        return train_test_split(X, y, test_size=0.2, shuffle=False)

    # Function to train and predict using Linear Regression
    def predict_stock_price(data, sentiment_data):
        X_train, X_test, y_train, y_test = prepare_data(data, sentiment_data)
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return model, predictions, mse, X_train, X_test, y_train, y_test


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []


    # Stock Market Prediction Section
    st.title("Stock Market Prediction Dashboard")

    symbol_input = st.text_input("Enter Stock Symbol (e.g., tata, apple, google, amazon)", "tata")

    # Map input to actual stock symbols
    symbol_mapping = {
        "tata": "TCS",
        "apple": "AAPL",
        "google": "GOOGL",
        "amazon": "AMZN"
    }
    symbol = symbol_mapping.get(symbol_input.lower())

    start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
    end_date = st.date_input("End Date", value=date.today())

    if symbol and start_date and end_date:
        data = get_stock_data(symbol, start=start_date, end=end_date)
        sentiment_data = get_sentiment_data(symbol, start=start_date, end=end_date)
        if not data.empty and not sentiment_data.empty:
            st.subheader(f"Stock Data for {symbol}")
            st.write(data.tail())
            st.line_chart(data['Close'])

            model, predictions, mse, X_train, X_test, y_train, y_test = predict_stock_price(data, sentiment_data)
            future_date = pd.to_datetime("2024-12-31").toordinal()
            future_sentiment = sentiment_data['Sentiment'].mean()  # Use average sentiment for future prediction
            future_prediction = model.predict([[future_date, future_sentiment]])

            st.subheader("Prediction Results")
            st.write(f"Mean Squared Error: {mse}")

            # Create a DataFrame to visualize the actual and predicted values
            actual_vs_predicted = pd.DataFrame(data={
                'Date': data.index[len(X_train):],
                'Actual': y_test,
                'Predicted': predictions
            })
            actual_vs_predicted.set_index('Date', inplace=True)

            st.line_chart(actual_vs_predicted)
            st.write(f"Predicted closing price for {symbol} on 2024-12-31: {future_prediction[0]}")

            stock_data_summary = f"Stock symbol: {symbol}\n\n"
            stock_data_summary += f"Prediction results: Mean Squared Error: {mse}\n"
            stock_data_summary += f"Predicted closing price for {symbol} on 2024-12-31: {future_prediction[0]}\n"

            st.subheader("Summary")
            st.write(stock_data_summary)

            st.subheader("Past Stock Data")
            st.dataframe(data)


 