import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

# Use seaborn theme for better visuals
sns.set_theme()

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
    
    # Bar chart for airline sentiment using Altair
    st.write("### Airline Sentiment Bar Chart")
    bar_chart = alt.Chart(sentiment_counts.reset_index()).mark_bar(color='skyblue').encode(
        x=alt.X('index:N', title='Sentiment'),
        y=alt.Y('airline_sentiment:Q', title='Count')
    ).properties(
        title='Airline Sentiment Bar Chart'
    )
    st.altair_chart(bar_chart, use_container_width=True)
    
    # Pie chart for airline sentiment using Altair
    st.write("### Airline Sentiment Pie Chart")
    pie_chart = alt.Chart(sentiment_counts.reset_index()).mark_arc().encode(
        theta=alt.Theta(field="airline_sentiment", type="quantitative"),
        color=alt.Color(field="index", type="nominal", scale=alt.Scale(scheme='pastel'))
    ).properties(
        title='Airline Sentiment Distribution'
    )
    st.altair_chart(pie_chart, use_container_width=True)

    # Bar chart for tweets count by airlines using Altair
    st.write("### Tweets Count by Airline")
    airline_counts = tweets['airline'].value_counts()
    sorted_airline_counts = airline_counts.sort_values(ascending=False).reset_index()
    bar_chart_airlines = alt.Chart(sorted_airline_counts).mark_bar().encode(
        x=alt.X('index:N', title='Airline', sort='-y'),
        y=alt.Y('airline:Q', title='Number of Tweets'),
        color=alt.Color(field='index', type='nominal', scale=alt.Scale(scheme='viridis'))
    ).properties(
        title='Tweets Count by Airline'
    )
    st.altair_chart(bar_chart_airlines, use_container_width=True)

else:
    st.write("Please upload a CSV file to continue.")
