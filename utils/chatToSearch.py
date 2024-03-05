import os
import getpass

import streamlit as st

# Gemini API
import google.generativeai as genai
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchRun

# api_key = os.getenv("GEMINI_API_KEY")
api_key = "AIzaSyAIDOlnc6NVX9LCwvNNuF6zXqBWplJsVpM"

genai.configure(api_key=api_key)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def getSearchResult(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.info("Please add your GEMINI API key to continue.")
        st.stop()

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

    with st.spinner('Asking to GEMINI...'):
        result = llm.invoke(prompt)

        search = DuckDuckGoSearchRun(name="Search")
        search_agent = initialize_agent(
            [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            return response
