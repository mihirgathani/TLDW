import torch
import pandas as pd      
from sentence_transformers import SentenceTransformer, util
import pandas as pd

def getBertRecs(user_transcript):
    # Load pre-trained SBERT model
    model_name = 'stsb-roberta-large'
    model = SentenceTransformer(model_name)

    # Load preprocessed TED Talks embeddings
    ted_embeddings = torch.load('ted_sbert_embeddings.pt')

    # Sample data (replace with your actual data)
    #df = pd.read_csv(r"C:\Users\mihir\Downloads\Check_TED.csv")
    df = pd.read_csv(r"C:\Users\mihir\Downloads\ted_talks_en.csv\ted_talks_en.csv")
    ted_talks_titles = df["title"].tolist()  # List of titles of TED Talks

    # Generate SBERT embedding for the user transcript
    user_embedding = model.encode(user_transcript)

    # Calculate cosine similarity between the user transcript embedding and all TED Talks embeddings
    similarities = util.cos_sim(user_embedding, ted_embeddings)

    # Create a DataFrame with TED Talks titles, descriptions, and cosine similarities
    ted_talks_df = pd.DataFrame({'title': ted_talks_titles, 'cosine_similarity': similarities.flatten()})

    # Get top 3 recommendations based on cosine similarity
    top_recommendations = ted_talks_df.nlargest(3, 'cosine_similarity')

    # Print top 3 recommendations
    print("-------------------------------------------------------------")
    print("Top 3 Recommendations - SBERT:")
    i = 1
    for index, row in top_recommendations.iterrows():
        print(f"Recommendation {i}")
        print(f"Title: {row['title']}")
        print(f"Similarity Score: {row['cosine_similarity']}")
        i += 1
        print()
