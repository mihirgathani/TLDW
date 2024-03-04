import torch
from transformers import BertTokenizer, BertModel
import pandas as pd

from sentence_transformers import SentenceTransformer, util
import pandas as pd

def preprocess_bert():
    # Load pre-trained SBERT model
    model_name = 'stsb-roberta-large'
    model = SentenceTransformer(model_name)

    df = pd.read_csv(r"C:\Users\mihir\Downloads\ted_talks_en.csv\ted_talks_en.csv")
    ted_talks_descriptions = df["transcript"].tolist()  # List of transcripts of TED Talks

    # Generate SBERT embeddings for TED Talks dataset
    ted_embeddings = model.encode(ted_talks_descriptions, show_progress_bar=True)

    # Save the embeddings to a file
    torch.save(ted_embeddings, 'ted_sbert_embeddings.pt')

# ----------------------------------------------------------------

# def preprocess_bert():
#     # Load pre-trained BERT model and tokenizer
#     model_name = 'bert-large-uncased'
#     tokenizer = BertTokenizer.from_pretrained(model_name)
#     model = BertModel.from_pretrained(model_name)

#     df = pd.read_csv(r"C:\Users\mihir\Downloads\Check_TED.csv")
#     ted_talks_descriptions = df["transcript"].tolist()  # List of short descriptions of TED Talks

#     # Generate BERT embeddings for TED Talks dataset
#     ted_embeddings = []
#     for ted_transcript in ted_talks_descriptions:
#         # Split the transcript into chunks based on its length
#         tokenized_chunks = tokenizer.tokenize(ted_transcript)
#         max_chunk_len = 512  # Maximum length for BERT input
#         chunks = [tokenized_chunks[i:i+max_chunk_len] for i in range(0, len(tokenized_chunks), max_chunk_len)]

#         # Generate BERT embeddings for each chunk and average them
#         chunk_embeddings = []
#         for chunk in chunks:
#             # Convert the chunk into tokens and pad if necessary
#             encoded_chunk = tokenizer.encode(chunk, add_special_tokens=True, max_length=max_chunk_len, truncation=True)
#             padded_chunk = encoded_chunk + [0] * (max_chunk_len - len(encoded_chunk))

#             # Convert the chunk into a tensor and generate embeddings
#             input_ids = torch.tensor(padded_chunk).unsqueeze(0)  # Add batch dimension
#             with torch.no_grad():
#                 outputs = model(input_ids)
#             chunk_embedding = outputs.last_hidden_state.mean(dim=1).squeeze()
#             chunk_embeddings.append(chunk_embedding)

#         # Average the embeddings of all chunks
#         ted_transcript_embedding = torch.stack(chunk_embeddings).mean(dim=0)
#         ted_embeddings.append(ted_transcript_embedding)

#     # Convert ted_embeddings list to a tensor
#     ted_embeddings_tensor = torch.stack(ted_embeddings)

#     # Save the embeddings tensor to a file
#     torch.save(ted_embeddings_tensor, 'ted_embeddings.pt')
