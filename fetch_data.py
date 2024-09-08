import requests
import streamlit as st

@st.cache_data
def get_recent_news(query):
    API_ENDPOINT = "ENDPOINT"

    headers = {
    "name": query,
    "Authorization": "API KEY" 
    }

    response = requests.request("GET", API_ENDPOINT,  headers=headers)

    return(response.json())