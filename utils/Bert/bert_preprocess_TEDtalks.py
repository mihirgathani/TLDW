import torch
import pandas as pd
from sentence_transformers import SentenceTransformer
import pandas as pd

def preprocess_bert(ted_or_podcast):

    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        df = pd.read_csv(r"C:\Users\mihir\Downloads\ted_talks_en.csv\ted_talks_en.csv") # Update file location
        transcripts = df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        df = pd.read_csv(r"C:\Users\mihir\Downloads\skeptoid_transcripts.csv\skeptoid_transcripts.csv") # Update file location
        transcripts = df["text"].tolist()  # List of transcripts

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
