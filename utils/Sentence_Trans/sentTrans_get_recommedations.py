import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# Function to get recommendations using precomputed embeddings
def getSentTransRecs(input_transcript, ted_or_podcast):
    
    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        df = pd.read_csv("../TLDW/ted_talks_en.csv") # Update file location
        with open('../TLDW/ted_sentTrans_embeddings.pkl', 'rb') as f:
            embeddings = pickle.load(f)
        transcripts = df["transcript"].tolist()
    else:
        # Load Podcast Dataset
        df = pd.read_csv("../TLDW/skeptoid_transcripts.csv") # Update file location
        with open('../TLDW/podcast_sentTrans_embeddings.pkl', 'rb') as f:
            embeddings = pickle.load(f)
        transcripts = df["transcript"].tolist()

    titles = df["title"].tolist()
    urls = df["url"].tolist()
    # Load Sentence Transformer model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)

    # Encode user input in chunks
    chunk_size = 256
    chunks = [input_transcript[i:i+chunk_size] for i in range(0, len(input_transcript), chunk_size)]
    user_input_embedding = np.mean([model.encode(chunk) for chunk in chunks], axis=0)

    # Compute cosine similarity between user input and TED transcripts
    similarity_scores = cosine_similarity([user_input_embedding], embeddings)[0]

    # Rank transcripts based on similarity scores
    ranked_transcripts = sorted(zip(titles, urls, similarity_scores), key=lambda x: x[1], reverse=True)

    # Get top 3 recommendations
    top_recommendations = ranked_transcripts[:3]
    top_recommendations_df = pd.DataFrame(top_recommendations, columns=["title", "url", "cosine_similarity"])

    return top_recommendations_df

    # Print top 3 recommendations
    #print("-------------------------------------------------------------")
    #print(f"Top 3 Recommendations for {ted_or_podcast} - Model all-MiniLM-L6-v2:")
    #for i, (recommendation, similarity_score) in enumerate(top_recommendations, 1):
        #print(f"Recommendation {i}")
        #print(f"Title: {recommendation}")
        #print(f"Similarity Score: {similarity_score}")
        #print()
