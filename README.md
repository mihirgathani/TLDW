<img width="880" alt="Screenshot 2024-03-12 at 11 27 06 AM" src="https://github.com/JoobeeJung/TLDW/assets/77033306/53aee74d-8966-4844-9433-3035dbe68e5f">

# UW MSDS DATA515: <br/> Summarization and Recommendation Tool with LLMs
![Build/Test Workflow](https://github.com/JoobeeJung/TLDW/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/JoobeeJung/TLDW/badge.svg?branch=main)](https://coveralls.io/github/JoobeeJung/TLDW?branch=main)

## Introduction
As students, we faced many challenges navigating YouTube's content landscape for learning purposes. With so many videos available on a wide range of topics, it was often overwhelming to find the most relevant and high-quality content. We found ourselves spending a significant amount of time sifting through videos, trying to identify those that would provide us with the insights and knowledge we were seeking.

This experience led us to recognize the need for a solution to streamline the learning process and make it more efficient. That's where TL;DW comes in. TL;DW, which stands for 'Too Long; Don't Watch,' is an innovative tool designed to address these challenges by summarizing YouTube videos and recommending supplementary TED Talks and podcasts.

With TL;DW, users no longer have to spend hours watching lengthy videos to extract key information. Instead, they can access concise summaries that capture the essence of the content in a fraction of the time. Additionally, TL;DW goes beyond simply summarizing videos by recommending supplementary content from TED Talks and podcasts, providing users with access to diverse perspectives and expertise on the topics they are interested in.

Team Members: 
| **Name**       | **Github**         |
|----------------|--------------------|
| Joobee Jung    | @JoobeeJung        |
| Mihir Gathani  | @mihirgathani      |
| Anurag Agarwal | @anuragagarwal1910 |
| Trisha Prasant | @trishaprasant     |

**Table of Contents**
1. [Introduction](#introduction)
2. [Tasks of Interest](#tasksofinterest)
3. [Repository Structure](#repostructure)
4. [Installation](#installation)
5. [Example](#example)

## Tasks of Interest
- **Youtube Video Summary and Keyword Generator**
  * This feature allows the user to input a YouTube link and extract key insights and main themes from the YouTube video transcript. It does so by providing a concise summary of the video alongside top 10 relevant keywords.
- **Recommendation System for TED Talks and Podcasts**
  * This feature allows the user to select whether they want to get recommendations for TED talks or podcasts based on their provided YouTube video. It then let's the user choose between 3 different models to get the top 3 recommendations. 
- **Chatbot to learn more content**
  * This feature enables a conversational AI interface that engages users in natural language interactions, allowing them to learn more about specific aspects of the content, explore related topics, and receive informative responses in real time.

## Questions of Interest
- What Ted Talks or Podcasts can I watch to learn more about the YouTube video I just watched?
- Can you give me a summary of the YouTube video that I watched?
- What does it mean when the video mentions this [topic]?
       
## Data Sources
- Youtube Transcript API: to obtain transcripts of a YouTube video based on its link
- Ted Talks Transcript: https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset 
- Podcast Transcript Dataset: https://www.kaggle.com/datasets/sentinel3734/skeptoid-podcast-transcripts
- [Gemini API](https://ai.google.dev/): to generate summary and keywords from the inputted YouTube video link. Also used for the chatbot.

## Repository Structure 
```
└── 📁TLDW
    └── .DS_Store
    └── .env
    └── 📁.github
        └── 📁workflows
            └── build_test.yml
    └── .gitignore
    └── LICENSE
    └── README.md (Current File)
    └── 📁TLDW
        └── .DS_Store
        └── 📁data
            └── podcast_sbert_embeddings.pt
            └── podcast_sentTrans_embeddings.pkl
            └── podcast_tdidf_preprocessed.csv
            └── podcast_tfidf_vectorizer.joblib
            └── skeptoid_transcripts.csv
            └── ted_sbert_embeddings.pt
            └── ted_sentTrans_embeddings.pkl
            └── ted_talks_en.csv
            └── ted_tdidf_preprocessed.csv
            └── ted_tfidf_vectorizer.joblib
        └── main.py
        └── streamlit_app.py
        └── 📁tests
            └── .DS_Store
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-311.pyc
                └── streamlit-tests.cpython-311.pyc
                └── test_streamlit_app.cpython-311.pyc
            └── test_bert_get_recommendations.py
            └── test_bert_preprocess.py
            └── test_helper_load_validate.py
            └── test_minilm_get_recommendations.py
            └── test_minilm_preprocess.py
            └── 📁test_output
                └── test_podcast_sbert_embeddings.pt
                └── test_podcast_sentTrans_embeddings.pkl
                └── test_podcast_tdidf_preprocessed.csv
                └── test_podcast_tfidf_vectorizer.joblib
                └── test_ted_sbert_embeddings.pt
                └── test_ted_sentTrans_embeddings.pkl
                └── test_ted_tdidf_preprocessed.csv
                └── test_ted_tfidf_vectorizer.joblib
            └── test_process_transcripts.py
            └── test_streamlit_app.py
            └── test_summarize_transcripts.py
            └── test_tdidf_get_recommendations.py
            └── test_tdidf_preprocess.py
            └── user_transcript1.txt
        └── 📁utils
            └── .DS_Store
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-311.pyc
                └── bert_get_recommendations.cpython-311.pyc
                └── bert_preprocess.cpython-311.pyc
                └── chatToSearch.cpython-311.pyc
                └── chat_to_search.cpython-311.pyc
                └── helper_load_validate.cpython-311.pyc
                └── minilm_get_recommedations.cpython-311.pyc
                └── minilm_preprocess.cpython-311.pyc
                └── processTranscripts.cpython-311.pyc
                └── process_transcripts.cpython-311.pyc
                └── summarizeTranscripts.cpython-311.pyc
                └── summarize_transcripts.cpython-311.pyc
                └── tdidf_get_recommendations.cpython-311.pyc
                └── tdidf_preprocess.cpython-311.pyc
                └── validation.cpython-311.pyc
            └── bert_get_recommendations.py
            └── bert_preprocess.py
            └── chat_to_search.py
            └── helper_load_validate.py
            └── minilm_get_recommedations.py
            └── minilm_preprocess.py
            └── process_transcripts.py
            └── summarize_transcripts.py
            └── tdidf_get_recommendations.py
            └── tdidf_preprocess.py
    └── 📁docs
        └── Component_Specifications.md
        └── FunctionalSpecification.md
        └── Milestones.md
        └── Technology Reviews.pdf
        └── final_diagram.png
        └── recommendation_module.png
        └── summarizer_module.png
        └── yttranscript_module.png
    └── environment.yml
    └── 📁examples
        └── Imp.md
        └── README.md
        └── 📁images
            └── chat_bot.png
            └── env.png
            └── home_page.png
            └── input_url.png
            └── keywords.png
            └── podcasts_recommendations.png
            └── summary.png
            └── tedtalks_recommendation.png
        └── website_navigation.md
    └── pyproject.toml
    └── requirements.txt
```

# Installation
This repository can be cloned locally using the following command.

```
git clone https://github.com/JoobeeJung/TLDW.git
```

*Note: Git is required to run the above command. For instructions on downloading Git, please see the [GitHub guide](https://github.com/git-guides/install-git).*


## Environment
Our application is built on various Python packages with specific version requirements. Installing these packages individually can cause conflicts and require dependencies in your workspace. To fix this issue, it is recommended to use a virtual environment in `conda` with all the necessary packages of our application. A list of necessary packages and libraries can be found in our [environment.yml](https://github.com/JoobeeJung/TLDW/blob/main/environment.yml) file and our [requirements.txt](https://github.com/JoobeeJung/TLDW/blob/main/requirements.txt) file.

To create a new `TLDW` Conda environment, run the following command:

```
conda env create -f environment.yml
```

Once the Conda environment is created, it can be activated by:

```
conda activate TLDW
```

The environment can be deactivated with the command:

```
conda deactivate
```

*Note: Conda is required to run the above command. For instructions on downloading Conda, please see the [Conda guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).*

## Application
We developed this application using the open-source `streamlit` package. A local application can be generated with the code:

```
conda activate TLDW
cd TLDW/TLDW
streamlit run streamlit_app.py
```

This will open a new tab in your browser with our functioning web application. More details can be found [here](https://github.com/JoobeeJung/TLDW/blob/main/examples/README.md).

## API Keys
This is a [Google Drive](https://drive.google.com/file/d/1BO4r8aet1pkxneqkwDYSnGjORephlPWr/view?usp=sharing) link for an API key for Google API.

# Examples
A video demonstration of our application is linked here.
More details on how to run our code are linked [here](https://github.com/JoobeeJung/TLDW/blob/main/examples/README.md).

## Issues
There are some bugs related to Streamlit or the GEMINI API. These issues are linked to [Github Issues](https://github.com/JoobeeJung/TLDW/issues) on this repository. 


