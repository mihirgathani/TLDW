# Overview
This is the main package for deploying the TL;DW web application. This folder contains the following;

- `./data/`: contains the data needed to populate the recommendation systems (both TED Talks and Podcasts)
- `./tests/`: contains unit tests and functional tests for all package-accessible code (all those in `./utils/`)
- `./utils/`: contains the files needed to generate transcripts, summaries, and keywords for a given YouTube video and train our recommendation system modules. 
  - `bert_get_recommendations.py`: module with functions to get recommendations based on user transcripts using Roberta embeddings. It generates Roberta embeddings for a given transcript, calculates cosine similarity between the transcript embedding and preprocessed Roberta embeddings of TED Talks or Podcasts, and returns the top 3 recommendations based on cosine similarity.
  - `bert_preprocess.py`: module provides preprocessing function to create embeddings for the Roberta model.
  - `chat_to_search.py`:  module implements the Gemini chatbot feature into the main interface.
  - `helper_load_validate.py`: module provides functions to validate if the correct input is provided to a function and to load the required data and transcripts.
  - `minilm_get_recommedations.py`: module with functions to get recommendations based on user transcripts using MiniLM embeddings. It generates MiniLM embeddings for a given transcript, calculates cosine similarity between the transcript embedding and preprocessed MiniLM embeddings of TED Talks or Podcasts, and returns the top 3 recommendations based on cosine similarity.
  - `minilm_preprocess.py`: module provides preprocess_minilm function that will create embeddings based on input arguments.
  - `process_transcripts.py`: provides functions to process transcripts from YouTube videos.
  - `summarize_transcripts.py`: module for summarizing transcripts using Gemini AI API.
  - `tdidf_get_recommendations.py`: module with functions to get recommendations based on user transcripts using TF-IDF embeddings. It generates TF-IDF embeddings for a given transcript, calculates cosine similarity between the transcript embedding and preprocessed TF-IDF embeddings of TED Talks or Podcasts, and returns the top 3 recommendations based on cosine similarity.
  - `tdidf_preprocess.py`: module provides preprocess_tdidf function to create embeddings based on input arguments.
- `streamlit_app.py`: contains the code that generates our Streamlit application.

