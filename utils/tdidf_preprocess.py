"""
Module: tdidf_preprocess
Description:
This module provides preprocess_tdidf function that will create embeddings based on input arguments.
It loads either TED Talks or Podcast transcripts, encodes them using tdidf vectorizer and saves the
embeddings to a file.
"""

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from . import validation

def preprocess_tdidf(ted_or_podcast):
    """
    This file preprocesses the ted talks/ podcasts and creates the embedding files for each using
    tdidf vectorizer.
    It is run only once for each, ted and podcast to create the embedding files, and not run again
    unless the original dataset has changed.

    Parameters:
    - ted_or_podcast (str): Type of data to preprocess. Should be either 'ted' or 'podcast'.

    Raises:
    - TypeError: If ted_or_podcast is not a string.
    - ValueError: If ted_or_podcast is neither 'ted' nor 'podcast'.

    Returns:
    None
    """

    validation.validate_ted_or_podcast(ted_or_podcast)

    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        filepath = "./ted_talks_en.csv"
        data_df = pd.read_csv(filepath)
        transcripts = data_df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        filepath = "./skeptoid_transcripts.csv"
        data_df = pd.read_csv(filepath)
        data_df = data_df.dropna(subset=["text"])
        transcripts = data_df["text"].tolist()  # List of transcripts

    tfidf_vectorizer = TfidfVectorizer()
    tokenized_transcripts = tfidf_vectorizer.fit_transform(transcripts)

    data_df['token'] = (
    [" ".join(tokens) for tokens in tfidf_vectorizer.inverse_transform(tokenized_transcripts)])

    # Save the preprocessed DataFrame and TF-IDF vectorizer to files
    if ted_or_podcast == "ted":
        data_df.to_csv('ted_tdidf_preprocessed.csv', index=False)
        joblib.dump(tfidf_vectorizer, 'ted_tfidf_vectorizer.joblib')
    else:
        data_df.to_csv('podcast_tdidf_preprocessed.csv', index=False)
        joblib.dump(tfidf_vectorizer, 'podcast_tfidf_vectorizer.joblib')
