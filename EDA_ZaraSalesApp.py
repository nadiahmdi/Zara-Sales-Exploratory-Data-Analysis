# -*- coding: utf-8 -*-
"""EDA_ZaraSalesApp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RBb48CYrQyktovL_dF4J5SWu3VZYXNOx
"""

#!pip install streamlit
import nltk
nltk.download('vader_lexicon')

import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Importing the dataset
store_zara = pd.read_csv("/content/store_zara.csv")

# Title of the application
st.title('Exploratory Data Analysis (EDA) on Zara_Sales')

# Display the dataset
st.subheader('Data Summary')
st.write(store_zara.head())

# Data Cleaning Section
st.subheader('Data Cleaning')

# Handling missing values
st.write("Handling missing values...")
# Your code for handling missing values here

# Removing duplicate rows
st.write("Removing duplicate rows...")
# Your code for removing duplicate rows here

# Descriptive Statistics Section
st.subheader('Descriptive Statistics')

# Summary statistics
st.write("Summary statistics:")
st.write(store_zara[['price']].describe())

# Histogram of 'price'
st.write("Distribution of Prices:")
plt.figure(figsize=(5, 4))
sns.histplot(store_zara['price'], bins=20, kde=True, color='blue')
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
st.pyplot()

# Count plot of 'currency'
st.write("Distribution of Currency:")
plt.figure(figsize=(2, 4))
sns.countplot(data=store_zara, x='currency', color='blue')
plt.title('Distribution of Currency')
plt.xlabel('Currency')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()

# Add more EDA visualizations and analysis as needed

# Sentiment Analysis Section
st.subheader('Sentiment Analysis')

# Sentiment analysis on product names
st.write("Sentiment analysis on product names:")
# Your code for sentiment analysis on product names here

# Sentiment analysis on product descriptions
st.write("Sentiment analysis on product descriptions:")
# Your code for sentiment analysis on product descriptions here

# Plotting sentiment analysis results
st.write("Sentiment analysis results:")
# Your code for plotting sentiment analysis results here

# Display the Streamlit app
if __name__ == '__main__':
    st.write("Streamlit App is running...")

