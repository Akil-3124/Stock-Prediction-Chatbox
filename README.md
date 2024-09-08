<p align="center">
    <h1 align="center">STOCK-PREDICTION-CHATBOX</h1>
</p>

<p align="center">
	<img src="https://img.shields.io/github/last-commit/Akil-3124/Stock-Prediction-Chatbox?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Akil-3124/Stock-Prediction-Chatbox?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Akil-3124/Stock-Prediction-Chatbox?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)

---

## 📍 Overview

<p>Welcome to the Stock Market Prediction and Analysis Dashboard! This application leverages advanced AI-driven technologies, including OpenAI's GPT models, LangChain, and sentiment analysis tools, to provide real-time stock market insights, predictions, and comprehensive data visualization.</p>

---

## 👾 Features

<p><b>Stock Market Prediction Dashboard:</b> Use AI-driven models to predict future stock prices based on historical data and sentiment analysis.<br>
<b>Current Price Analysis:</b> Fetch and visualize current stock prices for multiple stocks with interactive charts.<br>
<b>Recent News Insights:</b> Access the latest news related to specific stocks or market sectors to stay updated with market trends.<br>
<b>AI Chat Assistant:</b> Chat with an AI assistant to get personalized stock predictions, insights, and analysis based on the latest data and market sentiment.<br>
<b>Company Profiles:</b> Explore detailed profiles of companies, including financial metrics, risk analysis, and industry comparisons.<br>
</p>

---

## 📂 Repository Structure

```sh
└── Stock-Prediction-Chatbox/
    ├── chat.py
    ├── chatbox1.py
    ├── company.py
    ├── fetch_data.py
    ├── linechart.py
    ├── main.py
    └── recentnews.py
```

---

## 🧩 Modules

<details closed><summary>Here's a list of the key modules used in your Streamlit application along with a brief explanation of their purposes:

## Modules and Their Purposes<br>

### 1. **Streamlit (`streamlit`)**
   - **Purpose**: A Python library used for creating interactive web applications with a focus on data visualization and analysis. It simplifies the process of creating dashboards and web interfaces for data-driven projects.
   - **Usage**: To build the UI components like text inputs, buttons, charts, and to handle user interactions.

### 2. **Pandas (`pandas`)**
   - **Purpose**: A powerful data manipulation and analysis library. It provides data structures and operations for manipulating numerical tables and time series.
   - **Usage**: To handle and process stock market data, including reading, cleaning, and manipulating datasets.

### 3. **Requests (`requests`)**
   - **Purpose**: A simple HTTP library for making requests to web services and APIs.
   - **Usage**: To fetch data from external APIs, such as stock prices, company information, and recent news.

### 4. **LangChain (`langchain`)**
   - **Purpose**: A framework for developing applications powered by language models. It simplifies the process of integrating language models like GPT-3 or GPT-4 into applications.
   - **Usage**: To set up the AI chat functionality, which answers user queries based on stock data and market insights.

### 5. **LangChain Groq (`langchain_groq`)**
   - **Purpose**: A module that extends LangChain for Groq-based AI interactions, which might be used to optimize specific language model tasks.
   - **Usage**: For optimizing the performance of the AI-driven chat assistant in the application.

### 6. **OpenAI (`openai`)**
   - **Purpose**: The official Python client for OpenAI's GPT models and other AI services.
   - **Usage**: To interface with OpenAI's GPT models for generating responses to user queries in the chat section.

### 7. **VADER Sentiment (`vaderSentiment`)**
   - **Purpose**: A sentiment analysis tool that uses a lexicon and rule-based sentiment analysis engine specifically tuned for social media.
   - **Usage**: To analyze the sentiment of stock-related news, which can be used as a feature in stock price predictions.

### 8. **Scikit-learn (`sklearn`)**
   - **Purpose**: A machine learning library that includes simple and efficient tools for data analysis and modeling.
   - **Usage**: To perform linear regression modeling and predict stock prices based on historical data and sentiment analysis.

### 9. **yFinance (`yfinance`)**
   - **Purpose**: A Python library that wraps Yahoo Finance APIs for easy access to historical market data, including stock prices.
   - **Usage**: To fetch historical stock data that is used for analysis and prediction within the application.

### 10. **Altair (`altair`)**
   - **Purpose**: A declarative statistical visualization library for Python, based on Vega and Vega-Lite visualization grammars.
   - **Usage**: To create interactive charts for data visualization, such as bar charts for comparing stock prices.

### 11. **Streamlit Components (`streamlit.components.v1`)**
   - **Purpose**: Allows embedding and creating custom Streamlit components such as iframes and other HTML-based widgets.
   - **Usage**: To embed external content, such as Lottie animations for enhancing the UI.

### 12. **Streamlit Option Menu (`streamlit_option_menu`)**
   - **Purpose**: A library that provides a customizable sidebar menu for Streamlit applications.
   - **Usage**: To create a navigable sidebar for switching between different application pages like Dashboard, Current Price, Recent News, AI Chat, and Company Profile.

### 13. **Datetime (`datetime`)**
   - **Purpose**: A built-in Python module for manipulating dates and times.
   - **Usage**: To handle date inputs and format dates for fetching stock data within specified time ranges.

### 14. **Fetch Data Module (`fetch_data`)**
   - **Purpose**: A custom module created for fetching data from APIs related to stock prices, recent news, company profiles, etc.
   - **Usage**: Modularizes data fetching logic, allowing the main application code to remain clean and focused on user interaction and visualization.

## How to Use These Modules

- **Installation**: Install these modules using pip with the following command:
  ```bash
  pip install streamlit pandas requests langchain openai vaderSentiment scikit-learn yfinance altair
  ```
  Make sure to check for specific versions if required, and add any additional setup steps for proprietary or API-based modules (e.g., setting up API keys for OpenAI).

This list covers the main modules and their purposes, helping users understand the dependencies required for your application to run smoothly.</summary>

| File | Summary |
| --- | --- |
| [main.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/main.py) | <code>❯ REPLACE-ME</code> |
| [linechart.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/linechart.py) | <code>❯ REPLACE-ME</code> |
| [chatbox1.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/chatbox1.py) | <code>❯ REPLACE-ME</code> |
| [company.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/company.py) | <code>❯ REPLACE-ME</code> |
| [chat.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/chat.py) | <code>❯ REPLACE-ME</code> |
| [fetch_data.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/fetch_data.py) | <code>❯ REPLACE-ME</code> |
| [recentnews.py](https://github.com/Akil-3124/Stock-Prediction-Chatbox/blob/main/recentnews.py) | <code>❯ REPLACE-ME</code> |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

Python: `version 3.8 or higher`<br>
Streamlit<br>
Pandas<br>
yfinance<br>
requests<br>
scikit-learn<br>
altair<br>
vaderSentiment<br>
LangChain<br>
OpenAI API access<br>
Streamlit Option Menu<br>

### 📦 Installation

Build the project from source:

1. Clone the Stock-Prediction-Chatbox repository:
```sh
❯ git clone https://github.com/Akil-3124/Stock-Prediction-Chatbox
```

2. Navigate to the project directory:
```sh
❯ cd Stock-Prediction-Chatbox
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

### 🧪 Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

## 📌 Project Roadmap

Here's a detailed project roadmap for your Stock Market Prediction and Analysis application built with Streamlit. This roadmap outlines the major phases and tasks involved in developing, testing, and deploying the application.

## Project Roadmap

### Phase 1: Planning and Requirements Gathering
1. **Define Project Goals**
   - Set the primary objectives, such as providing stock market predictions, AI chat assistance, and company profiling.
   - Identify the key features needed for the application.

2. **Gather Requirements**
   - Define the data sources (e.g., Yahoo Finance, stock market APIs).
   - Identify the AI models and APIs (e.g., OpenAI's GPT-4).
   - Determine the tools and technologies (e.g., Streamlit, LangChain).

3. **Research and Analysis**
   - Explore similar tools in the market to identify gaps and improvements.
   - Research suitable machine learning models for stock prediction.

### Phase 2: Design and Architecture
1. **Design Application Architecture**
   - Define the overall architecture, including frontend (Streamlit) and backend (APIs, ML models).
   - Create data flow diagrams to map out how data will be processed and used.

2. **UI/UX Design**
   - Design wireframes and mockups for the dashboard, chat interface, and other pages.
   - Focus on user experience for easy navigation and interaction.

### Phase 3: Setup and Environment Configuration
1. **Set Up Development Environment**
   - Install necessary libraries and tools (`streamlit`, `pandas`, `requests`, etc.).
   - Configure environment variables and API keys for accessing external services.

2. **Version Control Setup**
   - Initialize a Git repository and set up version control.
   - Define branching strategy (e.g., main, develop, feature branches).

### Phase 4: Core Development
1. **Develop Core Features**
   - **Stock Prediction Model**: Implement machine learning models for stock price predictions using historical data and sentiment analysis.
   - **AI Chat Assistant**: Integrate OpenAI’s GPT-4 for answering user queries and providing insights.
   - **Data Fetching Module**: Create modules to fetch real-time stock data, recent news, and company profiles.

2. **Build UI Components**
   - Develop the Streamlit UI for different sections like the dashboard, AI chat, and company profile.
   - Integrate Lottie animations and visual elements for a better user interface.

3. **Backend Integration**
   - Connect the frontend with backend services like APIs for data fetching and AI responses.
   - Ensure smooth data flow between the client-side and server-side components.

### Phase 5: Testing and Validation
1. **Unit Testing**
   - Test individual components such as data fetching, model predictions, and API interactions.
   - Use testing frameworks like `pytest` for structured testing.

2. **Integration Testing**
   - Test the integration of various modules to ensure they work cohesively.
   - Validate data consistency and accuracy of AI responses.

3. **User Acceptance Testing (UAT)**
   - Conduct UAT with a sample group of users to gather feedback.
   - Adjust features and UI based on user feedback to improve usability.

### Phase 6: Optimization and Refinement
1. **Performance Optimization**
   - Optimize loading times and performance of the application.
   - Ensure API requests are efficient and handle data caching where necessary.

2. **Refinement Based on Feedback**
   - Refine the UI/UX based on testing feedback.
   - Improve the accuracy of predictions and AI responses by tweaking models and prompts.

### Phase 7: Deployment
1. **Prepare for Deployment**
   - Set up a deployment environment (e.g., AWS, Heroku, Streamlit Cloud).
   - Ensure all environment variables and API keys are securely managed.

2. **Deploy Application**
   - Deploy the application to the chosen platform.
   - Conduct a final round of testing in the production environment.

### Phase 8: Post-Deployment
1. **Monitor and Maintain**
   - Set up monitoring tools to track application performance and errors.
   - Regularly update the application to incorporate new features and improvements.

2. **User Training and Documentation**
   - Provide user guides and documentation on how to use the application.
   - Offer training sessions or tutorials if needed.

3. **Gather User Feedback and Iterate**
   - Continuously collect user feedback to identify new features or improvements.
   - Plan for iterative updates based on feedback and changing market needs.

### Phase 9: Scaling and Expansion
1. **Expand Features**
   - Add additional features like more advanced predictive models, wider data coverage, or new market insights.
   
2. **Scale Application**
   - Scale the application to handle more users or integrate with additional data sources.
   - Optimize for larger datasets and more complex analyses.

This roadmap provides a structured approach to building your Stock Market Prediction and Analysis application, ensuring a thorough and systematic development process from start to finish.

---
