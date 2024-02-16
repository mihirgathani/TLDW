from utils import getTranscript, getSummary

def main():
    video_url = input("Please enter the YouTube video URL: ")
    transcript = getTranscript(video_url)
    summary = getSummary(transcript)


if __name__ == '__main__':
    main()
