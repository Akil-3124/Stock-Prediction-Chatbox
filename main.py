import streamlit as st
from streamlit_option_menu import option_menu
import chatbox1, linechart,recentnews,chat,company

st.set_page_config(
    page_title="Stock Predicition"
)

class multiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Prediction Dashboard',
                options=['Dashboard', 'Current Price','Recentnews','AI Chat','Company Profile'],
                default_index=1,
                 styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#85929E"},
                    "nav-link-selected": {"background-color": "blue"},}
            )
        if app == 'Dashboard':
            chatbox1.app()
        if app == 'Current Price':
            linechart.app()
        if app == 'Recentnews':
            recentnews.app()
        if app == 'AI Chat':
            chat.app()
        if app == 'Company Profile':
            company.app()

app = multiApp()
app.run()
