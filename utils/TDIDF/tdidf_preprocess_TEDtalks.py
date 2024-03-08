import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_TDIDF(ted_or_podcast):
    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        df = pd.read_csv(r"C:\Users\mihir\Downloads\ted_talks_en.csv\ted_talks_en.csv") # Update file location
        transcripts = df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        df = pd.read_csv(r"C:\Users\mihir\Downloads\skeptoid_transcripts.csv\skeptoid_transcripts.csv") # Update file location
        df = df.dropna(subset=["text"])
        transcripts = df["text"].tolist()  # List of transcripts

    tfidf_vectorizer = TfidfVectorizer()
    tokenized_transcripts = tfidf_vectorizer.fit_transform(transcripts)

    # Add tokens as a column
    df['token'] = [" ".join(tokens) for tokens in tfidf_vectorizer.inverse_transform(tokenized_transcripts)]

    # Save the preprocessed DataFrame and TF-IDF vectorizer to files
    if ted_or_podcast == "ted":
        df.to_csv('ted_tdidf_preprocessed.csv', index=False)
        joblib.dump(tfidf_vectorizer, 'ted_tfidf_vectorizer.joblib')
    else:    
        df.to_csv('podcast_tdidf_preprocessed.csv', index=False)
        joblib.dump(tfidf_vectorizer, 'podcast_tfidf_vectorizer.joblib')
