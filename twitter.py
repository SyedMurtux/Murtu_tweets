# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the tweets data
tweets = pd.read_csv('https://raw.githubusercontent.com/SyedMurtux/Murtu_tweets/refs/heads/main/Tweets.csv')

# Streamlit app title
st.title("Twitter Airline Sentiment Analysis")

# Display a sample of the data
st.header("Sample of the Dataset")
st.write(tweets.head())

# Display the shape of the dataset
st.header("Dataset Shape")
st.write(tweets.shape)

# Plot airline sentiment distribution as a pie chart
st.header("Airline Sentiment Distribution")
fig1, ax1 = plt.subplots(figsize=(8, 6))
tweets['airline_sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax1)
ax1.set_ylabel('')
st.pyplot(fig1)

# Plot bar chart for tweets count by airline, with different colors and descending order
st.header("Tweets Count by Airline")
# Count tweets per airline
airline_counts = tweets['airline'].value_counts()
# Sort airlines by tweet count in descending order
sorted_airline_counts = airline_counts.sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(12, 6))
colors = plt.cm.get_cmap('viridis', len(sorted_airline_counts))  # Use a colormap for variety
bars = ax2.bar(sorted_airline_counts.index, sorted_airline_counts.values, color=colors(range(len(sorted_airline_counts))))

# Customize the chart
ax2.set_xlabel("Airlines")
ax2.set_ylabel("Number of Tweets")
ax2.set_title("Tweets Count by Airline")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent labels from overlapping

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')

st.pyplot(fig2)

# Run the app with: streamlit run <filename>.py
