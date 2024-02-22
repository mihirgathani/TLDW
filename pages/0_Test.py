import streamlit as st
from utils import getTranscript, get_ai_extract

st.title("TL;DW")
st.caption("🚀 Get a TED Talk Recommendation based on your interest!")

title = st.text_input('Youtube URL', 'Input your interested YT video!')


txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

st.write(f'You wrote {len(txt)} characters.')


def main():
    # video_url = input("Please enter the YouTube video URL: ")
    transcript = getTranscript(title)
    summary, _, _ = get_ai_extract("Summarize the following transcript in 150 words: ", transcript)
    keywords, _, _ = get_ai_extract("Generate the top 10 most important keywords: ", transcript)
    print(summary)
    print(keywords)


if __name__ == '__main__':
    main()
