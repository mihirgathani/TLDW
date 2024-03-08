
import re

url = input('URL')

import re

def extract_video_id(youtube_link):

    
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    
    
    match = re.search(pattern, youtube_link)
    
    if match:
        return match.group(1)  # Return the video ID
    else:
        return None  # Return None if no match found

youtube_link = f"{url}"
video = extract_video_id(youtube_link)



YOUTUBE_DATA_API_KEY = 'AIzaSyBe0K97tu3vxPEFPgsWtDfZTpXtc_EUwjU'
GEMINI_API_KEY = 'AIzaSyAIDOlnc6NVX9LCwvNNuF6zXqBWplJsVpM'



import google.generativeai as genai

# YouTube Data API
import googleapiclient.discovery

# For displaying videos in Colab
from IPython.display import YouTubeVideo

# YT Transcripts
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Gemini API
import google.generativeai as genai

"""# Functions to Search YouTube"""

youtube = googleapiclient.discovery.build(serviceName='youtube', version='v3', developerKey=YOUTUBE_DATA_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)
genai_model = genai.GenerativeModel('gemini-pro')

class Search_Response:
    def __init__(self, search_response) -> None:
        self.prev_page_token = search_response.get('prevPageToken')
        self.next_page_token = search_response.get('nextPageToken')

        # items element contain list of videos
        items = search_response.get('items')

        self.search_results = []
        for item in items:
            search_result = Search_Result(item)
            self.search_results.append(search_result)
            
class Search_Result:
    def __init__(self, search_result) -> None:
        self.video_id=     search_result['id']['videoId']
        self.title=        search_result['snippet']['title']
        self.description=  search_result['snippet']['description']
        self.thumbnails=   search_result['snippet']['thumbnails']['default']['url']
            
def search_yt(query, max_results=5, page_token=None):

    # Reference: https://developers.google.com/youtube/v3/docs/search/list
    # Reference: https://developers.google.com/youtube/v3/guides/implementation/pagination
    request = youtube.search().list(
        part="snippet", # search by keyword
        maxResults=max_results,
        pageToken=page_token, # optional, for going to next/prev result page
        q=query,
        videoCaption='closedCaption', # only include videos with captions
        type='video',   # only include videos, not playlists/channels
    )
    response = request.execute()
    search_response = Search_Response(response)
    return search_response


def get_transcript(video_id, languages=['en','en-US','en-GB']):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    transcript = TextFormatter().format_transcript(transcript)

    # print(transcript)
    return transcript

# Extract information from text based on prompt instructions
def get_ai_extract(prompt, text):
    response = genai_model.generate_content(prompt + text, stream=False)
    return response.text, response.prompt_feedback, response.candidates

transcript = get_transcript('video')

summary, _, _ = get_ai_extract("Summarize the following transcript: ", transcript)
keywords, _, _ = get_ai_extract("Generate the important keywords: ", transcript)
print(summary)


class Search_Result:
    def __init__(self, search_result) -> None:
        self.video_id=     search_result['id']['videoId']
        self.title=        search_result['snippet']['title']
        self.description=  search_result['snippet']['description']
        self.thumbnails=   search_result['snippet']['thumbnails']['default']['url']

