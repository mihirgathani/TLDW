import torch
import pandas as pd      
from sentence_transformers import SentenceTransformer, util

def getBertRecs(user_transcript, ted_or_podcast):
    # Load pre-trained SBERT model
    model_name = 'stsb-roberta-large'
    model = SentenceTransformer(model_name)

    if ted_or_podcast == "ted":
        # Load preprocessed TED Talks embeddings and TED Dataset
        embeddings = torch.load('../TLDW/ted_sbert_embeddings.pt')
        df = pd.read_csv("../TLDW/ted_talks_en.csv") # Update file location
    else:
        # Load preprocessed Podcast Talks embeddings and Podcast Dataset
        embeddings = torch.load('podcast_sbert_embeddings.pt')
        df = pd.read_csv("../TLDW/skeptoid_transcripts.csv") # Update file location

    titles = df["title"].tolist()  # List of titles

    # Generate SBERT embedding for the user transcript
    user_embedding = model.encode(user_transcript)

    # Calculate cosine similarity between the user transcript embedding and all TED Talks embeddings
    similarities = util.cos_sim(user_embedding, embeddings)

    # Create a DataFrame with TED Talks titles, descriptions, and cosine similarities
    ted_talks_df = pd.DataFrame({'title': titles, 'url': df['url'], 'cosine_similarity': similarities.flatten()})

    # Get top 3 recommendations based on cosine similarity
    top_recommendations = ted_talks_df.nlargest(3, 'cosine_similarity')
    return top_recommendations
    # Print top 3 recommendations
    #print("-------------------------------------------------------------")
    #print("Top 3 Recommendations - SBERT:")
    #i = 1
    #for index, row in top_recommendations.iterrows():
        #print(f"Recommendation {i}")
        #print(f"Title: {row['title']}")
        #print(f"Similarity Score: {row['cosine_similarity']}")
        #i += 1
        #print()
    #return top_recommendations
