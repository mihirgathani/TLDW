# Data Descriptions
For our application, we obtain data from three different sources. Their details can be found below:
- [Datasets](##Datasets)
  - [TED Talks Dataset](###TEDTalksDataset)
  - [Podcasts Dataset](##PodcastsDataset)
- [Embeddings](##GeneratedEmbeddings)
- [APIs](##APIs)

## Datasets
### TED Talks Dataset
Contains transcripts of TED Talks. Serves as a supplementary data source for recommending TED Talks related to the content of YouTube videos. To download this dataset for yourself, go to this [link](https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset). We have focused our analysis on obtaining and recommending TED Talks for English videos. Named `ted_talks_en.csv`. 

#### Data Dictionary for TED Talks Dataset
|    Attribute   |                   Description                  |  Data Type |
|:--------------:|:----------------------------------------------:|:----------:|
| talk_id        | Talk identification number provided by TED     | int        |
| title          | Title of the talk                              | string     |
| speaker_1      | First speaker in TED's speaker list            | string     |
| speakers       | Speakers in the talk                           | dictionary |
| occupations    | *Occupations of the speakers                   | dictionary |
| about_speakers | *Blurb about each speaker                      | dictionary |
| views          | Count of views                                 | int        |
| recorded_date  | Date the talk was recorded                     | string     |
| published_date | Date the talk was published to TED.com         | string     |
| event          | Event or medium in which the talk was given    | string     |
| native_lang    | Language the talk was given in                 | string     |
| available_lang | All available languages (lang_code) for a talk | list       |
| comments       | Count of comments                              | int        |
| duration       | Duration in seconds                            | int        |
| topics         | Related tags or topics for the talk            | list       |
| related_talks  | Related talks (key='talk_id', value='title')   | dictionary |
| url            | URL of the talk                                | string     |
| description    | Description of the talk                        | string     |
| transcript     | Full transcript of the talk                    | string     |

### Podcasts Dataset
Contains transcripts of podcasts. Provides additional content for recommending podcasts related to topics covered in YouTube videos. To download this dataset for yourself, go to this [link](https://www.kaggle.com/datasets/sentinel3734/skeptoid-podcast-transcripts). The transcripts and the associated metadata are collected from the Skeptoid website: https://skeptoid.com. Named `skeptoid_transcripts.csv`.

#### Data Dictionary for Podcasts Dataset
| Attribute        | Description                            | Data Type |
|:----------------:|:--------------------------------------:|:---------:|
| title            | The title of the episode               | string    |
| episode_number   | The episode number                     | int       |
| publication_date | The date the episode was released      | Date      |
| quote            | A one-line tweet-like description      | string    |
| by               | The author                             | string    |
| categories       | Categories the episode is listed under | list      |
| citation         | Citation for the episode               | string    |
| text             | The text of the transcript             | string    |
| url              | Link to the episode page               | string    |

## Generated Embeddings
We generate embeddings for the two datasets beforehand to facilitate live recommendations later, enabling quicker retrieval and comparison of similar content based on semantic similarity, thus enhancing the real-time user experience.
1. podcast_sbert_embeddings.pt: PyTorch file containing embeddings generated using Roberata model for podcast transcripts.
2. podcast_sentTrans_embeddings.pkl: Pickle file storing sentence-level embeddings obtained from minilm model for podcast transcripts.
3. podcast_tdidf_preprocessed.csv: Preprocessed CSV file of podcast transcripts after TF-IDF transformation.
4. podcast_tfidf_vectorizer.joblib: Joblib file storing TF-IDF vectorizer used for podcast transcript preprocessing.
5. ted_sbert_embeddings.pt: PyTorch file containing embeddings generated using Roberta model for TED talk transcripts.
6. ted_sentTrans_embeddings.pkl: Pickle file storing sentence-level embeddings obtained from minilm model for TED talk transcripts.
7. ted_tdidf_preprocessed.csv: Preprocessed CSV file of TED talk transcripts after TF-IDF transformation.
8. ted_tfidf_vectorizer.joblib: Joblib file storing TF-IDF vectorizer used for TED talk transcript preprocessing.

## APIs
**Youtube Transcript API**
To obtain transcripts of YouTube videos based on their links. This API provides access to textual content spoken in videos. This API is used in the `process_transcript.py` file in our `./utils/` module. The documentation for this library is found [here](https://pypi.org/project/youtube-transcript-api/)

**Gemini API**
To create summaries from inputted YouTube video links. The Gemini API allows us to easily analyze video content and generate concise summaries automatically. This API is used in the `summarize_transcripts.py` and `chat_to_search.py` in our `./utils/` module. Information for using this API can be found [here](https://ai.google.dev/). 



