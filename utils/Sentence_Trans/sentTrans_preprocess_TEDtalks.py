import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

def preprocess_sentTrans():
    # Load TED dataset
    df = pd.read_csv(r"C:\Users\mihir\Downloads\Check_TED.csv")
    ted_titles = df["title"].tolist()
    ted_transcripts = df["transcript"].tolist()

    # Load Sentence Transformer model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)

    # Create embeddings for TED transcripts and chunk them
    chunk_size = 256

    ted_embeddings = []
    for transcript in ted_transcripts:
        chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
        chunk_embeddings = [model.encode(chunk) for chunk in chunks]
        transcript_embedding = np.mean(chunk_embeddings, axis=0)
        ted_embeddings.append(transcript_embedding)

    # Save TED embeddings to a file
    with open('ted_sentTrans_embeddings.pkl', 'wb') as f:
        pickle.dump(ted_embeddings, f)
