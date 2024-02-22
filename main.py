from utils import getTranscript, get_ai_extract

def main():
    video_url = input("Please enter the YouTube video URL: ")
    transcript = getTranscript(video_url)
    summary, _, _ = get_ai_extract("Summarize the following transcript in 150 words: ", transcript)
    keywords, _, _ = get_ai_extract("Generate the top 10 most important keywords: ", transcript)
    print(summary)
    print(keywords)


if __name__ == '__main__':
    main()
