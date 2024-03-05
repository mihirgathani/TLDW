import streamlit as st
from utils import getTranscript, get_ai_extract, get_search_result

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

    st.divider()
    def example():
        want_to_contribute = st.button("I want to contribute!")
        if want_to_contribute:
            switch_page("Contribute")
            
    # Implemented Chatbot    
    st.header("🔎 Learn More - Chat with GEMINI ")

    """
    If you want to learn more about the content, feel free to ask GEMINI using this chat function!
    """

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Type any questions you have about the YouTube video."):
        st.write(get_search_result(prompt))
