from youtube_transcript_api import YouTubeTranscriptApi

DEBUG_MODE = False

def get_video_id(youtube_url):
    # Split the URL by "=" sign
    parts = youtube_url.split("v=")
    # Take the last part of the resulting list
    video_id = parts[-1]
    if DEBUG_MODE:
        print("Video ID: " + video_id)
    return video_id

def get_video_transcript(video_id):
    try:
        transcriptDict = YouTubeTranscriptApi.get_transcript(video_id)
        formattedTranscript = formatTranscript(transcriptDict)
        if DEBUG_MODE:
            print("Processed transcript: " + formattedTranscript)
        return formattedTranscript
    except Exception as e:
        print("Failed to get transcript")
        if DEBUG_MODE:
            print(f"Error: {e}")
        return None

def formatTranscript(transcriptDict):
    transcript_string = ""
    for item in transcriptDict:
        transcript_string += item['text'] + " "
    # Replace multiple spaces with a single space
    transcript_string = ' '.join(transcript_string.split())
    return transcript_string.strip()

def getTranscript(youtube_url):
    video_id = get_video_id(youtube_url)
    transcript = get_video_transcript(video_id)
    return transcript