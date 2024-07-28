import streamlit as st
import requests
import streamlit.components.v1 as com
import fetch_data

def app():
    st.title("Recent News")
    com.iframe("https://lottie.host/embed/b3294fc1-a9ad-412a-ae21-1aedb3818a0b/KJgOrkkpA9.json")
    st.write("Welcome to our AI Stock News Chatbox! Stay updated with the latest market news and trends through our advanced AI-driven platform. Receive real-time updates, personalized insights, and comprehensive news analysis to make informed investment decisions. Our chatbox also offers market sentiment analysis, helping you stay ahead of trends and make strategic investments based on the most current and relevant news.")
    
    news_query = st.text_input("Enter a query for recent news (e.g., stock name)")

    if news_query:
        news_results = fetch_data.get_recent_news(news_query).get("recentNews", [])
        if news_results:
            st.subheader("Recent News Results")
            for item in news_results:
                st.write(f"**Topic:** {item['headline']}")
                st.write(f"**Date:** {item['date']}")
                st.write(f"**For More Information:** [Click Here]({item['url']})")
                st.image(item['listimage'], caption=item['headline'])
                st.write("---")
        else:
            st.error("Failed to fetch recent news. Please try again later.")

