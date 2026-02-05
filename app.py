import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Sentiment Analysis ", page_icon="💬")

st.title("Sentiment Analysis App")
st.write("Classify text as **Positive**, **Negative**, or **Neutral** using LLM")

text = st.text_area("Enter your text:")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prompt = f"""
Analyze the sentiment of the following text.
Return only one word from these:
Positive, Negative, Neutral.

Text:
{text}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        sentiment = response.choices[0].message.content.strip()

        if sentiment.lower() == "positive":
            st.success("Sentiment: Positive 😊")
        elif sentiment.lower() == "negative":
            st.error("Sentiment: Negative 😞")
        else:
            st.info("Sentiment: Neutral 😐")

        st.write("**Output:**", sentiment)
