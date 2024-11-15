import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title for the Streamlit app
st.title('Twitter Airline Sentiment Analysis')

# Upload CSV file
st.write("### Upload the CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data into a DataFrame
    tweets = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the dataset
    st.write("### Preview of the Dataset")
    st.write(tweets.head())
    
    # Show dataset shape
    st.write("### Dataset Shape")
    st.write(tweets.shape)

    # Airline sentiment value counts
    st.write("### Airline Sentiment Distribution")
    sentiment_counts = tweets['airline_sentiment'].value_counts()
    st.write(sentiment_counts)
    
    # Bar chart for airline sentiment
    st.write("### Airline Sentiment Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.index, sentiment_counts)
    ax.set_title("Airline Sentiment Bar Chart")
    st.pyplot(fig)
    
    # Pie chart for airline sentiment
    st.write("### Airline Sentiment Pie Chart")
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    ax.set_title("Airline Sentiment Distribution")
    st.pyplot(fig)

else:
    st.write("Please upload a CSV file to continue.")
