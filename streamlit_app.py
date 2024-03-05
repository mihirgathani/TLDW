"""
Streamlit App for TED Talk Recommendations.

This app allows users to enter a YouTube URL, obtain the transcript,
summary, and keywords using Gemini, and get recommendations for TED Talks
using various recommendation algorithms.
"""

import streamlit as st
from utils import (getTranscript, get_ai_extract, getBertRecs,
                   getSentTransRecs, getTDIDFRecs, getSearchResult)

st.title("📝 TL;DW ")
st.caption("🚀 Get a TED Talk Recommendation based on your interest!")

# Function to create accordion-style recommendations
def create_accordion_recs(recommendations):
    """
    Creates an accordion-style display of recommendations.

    Args:
        recommendations (DataFrame): DataFrame containing recommendations with 
        columns 'title', 'url', and 'cosine_similarity'.

    Returns:
        None
    """
    i = 1
    for _, row in recommendations.iterrows():
        with st.expander(f"Recommendation {i}: {row['title']}"):
            st.markdown("- **URL:** " + row['url'])
            st.markdown("- **Similarity Score:** " + str(round(row['cosine_similarity'], 2)))
        i += 1

# Function to get transcript, summary, and keywords if not already obtained
def get_transcript_summary_keywords(link):
    """
    Retrieves transcript, summary, and keywords for the provided YouTube video link.

    Args:
        link (str): The YouTube video link.

    Returns:
        None
    """
    if 'transcript' not in st.session_state:
        with st.spinner('Getting transcript...'):
            st.session_state.transcript = getTranscript(link)
    if 'summary' not in st.session_state:
        with st.spinner('Summarizing using Gemini...'):
            st.session_state.summary, _, _ = get_ai_extract(
                "Summarize the following transcript in 150 words: ", st.session_state.transcript)
            st.success('Summary is ready!')
    if 'keywords' not in st.session_state:
        with st.spinner('Getting keywords using Gemini...'):
            st.session_state.keywords, _, _ = get_ai_extract(
                "Generate the top 10 most important keywords: ", st.session_state.transcript)
            st.success('Keywords are ready!')

# Starting information
st.info(
    """
    So... how does this work?  
        :one:  Enter a youtube link in the text box below.  
        :two:  Get a summary and keywords from Google's Gemini.  
        :three: Choose to get recommendations from either hundreds of TED Talks or Podcasts.  
        :four: Not satisfied? Test out our different models for different recommendations.  
    """,
    icon="👾",
)
# Get user input
title = st.text_input('Youtube URL')

# Check if user input is provided
if title:
    # Get transcript, summary, and keywords if not already obtained
    get_transcript_summary_keywords(title)

    # Display summary if available
    if 'summary' in st.session_state:
        st.header("Summary")
        st.write(st.session_state.summary)

    st.divider()

    # Display keywords if available
    if 'keywords' in st.session_state:
        st.header("Keywords")
        st.write(st.session_state.keywords)

    st.divider()

    st.write('Choose a recommender to get recommendations:')
    col1, col2, col3 = st.columns(3)

    # SBERT Recommender button
    if col1.button('SBERT Recommender', type='primary'):
        bert_recs = getBertRecs(st.session_state.transcript)
        if bert_recs is not None and not bert_recs.empty:
            st.header('Top 3 SBERT Recommendations')
            create_accordion_recs(bert_recs.head(3))

    # MiniLM Recommender button
    if col2.button('MiniLM Recommender', type='primary'):
        miniLM_recs = getSentTransRecs(st.session_state.transcript)
        if miniLM_recs is not None and not miniLM_recs.empty:
            st.header('Top 3 MiniLM Recommendations')
            create_accordion_recs(miniLM_recs.head(3))

    # TF-IDF Recommender button
    if col3.button('TF-IDF Recommender', type='primary'):
        tf_idf_recs = getTDIDFRecs(st.session_state.transcript)
        if tf_idf_recs is not None and not tf_idf_recs.empty:
            st.header('Top 3 TF-IDF Recommendations')
            create_accordion_recs(tf_idf_recs.head(3))

    st.header("🔎 Learn More - Chat with GEMINI ")
    st.write("If you want to learn more about the content, ask GEMINI using this chat function!")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content":
             "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Type any questions you have about the YouTube video."):
        st.write(getSearchResult(prompt))
