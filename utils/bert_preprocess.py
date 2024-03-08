"""
Module: bert_preprocess
Description:
This module provides preprocess_bert function that will create embeddings based on input arguments.
It loads either TED Talks or Podcast transcripts, encodes them using a pre-trained Roberta model,
and saves the embeddings to a file.
"""

import torch
import pandas as pd
from sentence_transformers import SentenceTransformer
from . import validation

def preprocess_bert(ted_or_podcast):
    """
    This file preprocesses the ted talks/ podcasts and creates the embedding files for each using
    Roberta model.
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
        ted_df = pd.read_csv(filepath)
        transcripts = ted_df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        filepath = "./skeptoid_transcripts.csv"
        podcast_df = pd.read_csv(filepath)
        transcripts = podcast_df["text"].tolist()  # List of transcripts

    # Load pre-trained Roberta model
    model_name = 'stsb-roberta-large'
    model = SentenceTransformer(model_name)

    # Generate Roberta embeddings for dataset
    embeddings = model.encode(transcripts, show_progress_bar=True)

    # Save the embeddings to a file
    if ted_or_podcast == "ted":
        torch.save(embeddings, 'ted_sbert_embeddings.pt')
    else:
        torch.save(embeddings, 'podcast_sbert_embeddings.pt')
