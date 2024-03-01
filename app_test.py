import streamlit as st
import time
from utils import getTranscript, get_ai_extract

st.title("📝 TL;DW ")
st.caption("🚀 Get a TED Talk Recommendation based on your interest!")

title = st.text_input('Youtube URL')

if title:
    with st.spinner('Getting transcript...'):
        transcript = getTranscript(title)
    st.success('Transcript is ready!')

    if transcript:
        st.header("Transcript")
        st.write(transcript)

    st.divider()

    with st.spinner('Summarizing using Gemini...'):
        summary, _, _ = get_ai_extract("Summarize the following transcript in 150 words: ", transcript)

    st.success('Summary is ready!')

    if summary:
        st.header("Summary")
        st.write(summary)

    st.divider()

    with st.spinner('Getting keywords using Gemini...'):
        keywords, _, _ = get_ai_extract("Generate the top 10 most important keywords: ", transcript)

    st.success('Keywords is ready!')

    if keywords:
        st.header("Keywords")
        st.write(keywords)
