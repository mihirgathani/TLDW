import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

def preprocess_sentTrans(ted_or_podcast):

    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        df = pd.read_csv("../TLDW/ted_talks_en.csv") # Update file location
        transcripts = df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        df = pd.read_csv("../TLDW/skeptoid_transcripts.csv") # Update file location
        transcripts = df["text"].tolist()  # List of transcripts

    # Load Sentence Transformer model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)

    # Create embeddings for TED transcripts and chunk them
    chunk_size = 256

    embeddings = []
    for transcript in transcripts:
        if type(transcript) == str:
            chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
            chunk_embeddings = [model.encode(chunk) for chunk in chunks]
            transcript_embedding = np.mean(chunk_embeddings, axis=0)
            embeddings.append(transcript_embedding)

    # Save embeddings to a file
    if ted_or_podcast == "ted":
        with open('../TLDW/ted_sentTrans_embeddings.pkl', 'wb') as f:
            pickle.dump(embeddings, f)
    else:
        with open('../TLDW/podcast_sentTrans_embeddings.pkl', 'wb') as f:
            pickle.dump(embeddings, f)