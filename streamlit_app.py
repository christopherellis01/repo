#!/usr/bin/env python3.8

import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        st.error(f"Failed to fetch content from {url}")
        return None

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract relevant information here; for example, extract all paragraphs
    paragraphs = soup.find_all('p')
    content = "\n\n".join([para.get_text() for para in paragraphs])
    return content

# Dictionary containing models
md = {
    'models': ['BeautifulSoup', 'Model B', 'Model C']
}

# Main title and welcome message
st.title("Writer's Assistant")
st.write("Welcome to the Writer's Assistant App!")
st.write("App URL: [writersassistant.streamlit.app](https://writersassistant.streamlit.app)")

# Sidebar for model selection and parameters
st.sidebar.header('Models')
model = st.sidebar.selectbox('Choose model:', md['models'])

st.sidebar.header('Parameters')
temp = st.sidebar.slider('Temperature:', 0.0, 1.0, 0.5)

st.session_state.model = model
st.session_state.temp = temp

# Fetch and display webpage content if BeautifulSoup model is selected
if model == 'BeautifulSoup':
    url = "https://w.amazon.com/bin/view/Users/chaeclrk/assets/generative-ai/AuthorsAssistantBedrockSageMaker"
    html_content = fetch_webpage_content(url)
    if html_content:
        content = extract_content(html_content)
        st.subheader("Content from the webpage (using BeautifulSoup):")
        st.write(content)
