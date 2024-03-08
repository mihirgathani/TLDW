import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def getTDIDFRecs(transcript_from_gemini):
    # Load preprocessed TED Talks data
    df = pd.read_csv('../TLDW/tdidf_ted_preprocessed.csv')

    # Load TF-IDF vectorizer
    tfidf_vectorizer = joblib.load('../TLDW/tfidf_vectorizer.joblib')

    
    # Generate TF-IDF vector for transcript from Gemini
    gemini_tfidf_matrix = tfidf_vectorizer.transform([transcript_from_gemini])

    # Calculate cosine similarity between Gemini's TF-IDF vector and TED Talks TF-IDF vectors
    cosine_similarities = cosine_similarity(gemini_tfidf_matrix, tfidf_vectorizer.transform(transcripts)).flatten()

    # Add cosine similarities as a column in the DataFrame
    df['cosine_similarity'] = cosine_similarities

    # Get top 3 recommendations based on cosine similarity
    top_recommendations = df.nlargest(3, 'cosine_similarity')

    # Print top 3 recommendations
    #print("-------------------------------------------------------------")
    #print("Top 3 Recommendations - TDIDF:")
    #for i in range(3):
        #print("Recommendation", i + 1)
        #print("Title:", top_recommendations.iloc[i]["title"])
        #print("Similarity Score:", top_recommendations.iloc[i]["cosine_similarity"])
        #print()
    return top_recommendations
