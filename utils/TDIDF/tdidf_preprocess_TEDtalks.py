import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_TDIDF():
    # Load TED Talks data
    df = pd.read_csv(r"C:\Users\mihir\Downloads\Check_TED.csv")
    
    # Tokenize the 'transcript' column
    tfidf_vectorizer = TfidfVectorizer()
    tokenized_transcripts = tfidf_vectorizer.fit_transform(df['transcript'])

    # Add tokens as a column
    df['token'] = [" ".join(tokens) for tokens in tfidf_vectorizer.inverse_transform(tokenized_transcripts)]

    # Save the preprocessed DataFrame and TF-IDF vectorizer to files
    df.to_csv('tdidf_ted_preprocessed.csv', index=False)
    joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.joblib')
