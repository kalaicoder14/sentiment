import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis", page_icon="💬")

st.title("Sentiment Analysis App")
st.write("Classify text as **Positive**, **Negative**, or **Neutral**")

text = st.text_area("Enter your text:")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            st.success("Sentiment: Positive 😊")
        elif polarity < 0:
            st.error("Sentiment: Negative 😞")
        else:
            st.info("Sentiment: Neutral 😐")

        st.write(f"**Polarity Score:** {polarity}")
