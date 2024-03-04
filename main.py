from utils import getTranscript, get_ai_extract, preprocess_bert, getBertRecs, preprocess_sentTrans, getSentTransRecs, preprocess_TDIDF, getTDIDFRecs

def main():
    video_url = input("Please enter the YouTube video URL: ")
    transcript = getTranscript(video_url)
    summary, _, _ = get_ai_extract("Summarize this transcript within 250 words, output a paragram: ", transcript)
    keywords, _, _ = get_ai_extract("Generate the top 10 most important keywords: ", transcript)
    print("This is the summary of the transcript:")
    print(summary)
    print("----------------------------------------------------------------")
    print("These are the top 10 keywords:")
    print(keywords)

    # sbert
    #preprocess_bert()
    getBertRecs(transcript)

    # sentence-transformer
    #preprocess_sentTrans()
    getSentTransRecs(transcript)

    # tdidf
    #preprocess_TDIDF()
    getTDIDFRecs(transcript)


if __name__ == '__main__':
    main()
