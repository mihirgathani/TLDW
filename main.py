from utils import getTranscript, get_ai_extract, preprocess_bert, getBertRecs, preprocess_sentTrans, getSentTransRecs, preprocess_TDIDF, getTDIDFRecs

def main():
    video_url = input("Please enter the YouTube video URL: ")
    transcript = getTranscript(video_url)
    summary, _, _ = get_ai_extract("Summarize this transcript within 250 words, output a paragraph: ", transcript)
    keywords, _, _ = get_ai_extract("Generate the top 10 most important keywords: ", transcript)
    print("This is the summary of the transcript:")
    print(summary)
    print("----------------------------------------------------------------")
    print("These are the top 10 keywords:")
    print(keywords)

    # Roberta
    # preprocess_bert("ted")
    getBertRecs(transcript, "ted")
    # preprocess_bert("podcast")
    getBertRecs(transcript, "podcast")

    # Sentence-transformer -> all-MiniLM-L6-v2
    # preprocess_sentTrans("ted")
    getSentTransRecs(transcript, "ted")
    # preprocess_sentTrans("podcast")
    getSentTransRecs(transcript, "podcast")

    # tdidf
    #preprocess_TDIDF("ted")
    getTDIDFRecs(transcript, "ted")
    #preprocess_TDIDF("podcast")
    getTDIDFRecs(transcript, "podcast")


if __name__ == '__main__':
    main()
