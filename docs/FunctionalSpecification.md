# Functional Specification
This document will provide information about the following sections: 
- **Background**: The problem being addressed
- **User profile**: Who uses the system? What they know about the domain and computing (e.g., can browse the web, can program in Python)
- **Data sources**: What data will you use, and how is it structured?
- **Use cases**: Describing at least two use cases.
  - For each use case, we will describe the objective of the user interaction and (b) the expected interactions between the user and your systems.
 
## Background
TL;DW is a web application designed to provide users with a summary of YouTube videos along with recommendations for TED Talks and podcasts related to the video content.

## User Profiles:
Some potential user profiles for this application are described below:
\
**User Profile 1: Tech Enthusiast**

- **Who**: A tech-savvy individual with a strong interest in the latest advancements in technology, science, and innovation.
- **Domain Knowledge**: Well-versed in navigating the web and comfortable with technology jargon. Likely familiar with YouTube's content and TED Talks. May have some understanding of programming concepts, such as Python.
- **Computing Skills**: Proficient in browsing the web, capable of using various online platforms effectively. Might have basic programming skills, enabling them to understand how functions of the TL;DW application.

**User Profile 2: Lifelong Learner**
- **Who**: A curious individual passionate about lifelong learning, personal development, and self-improvement.
- **Domain Knowledge**: May not be deeply immersed in technology but has a strong interest in accessing educational content online. Likely familiar with TED Talks as a source of insightful talks and ideas. Limited understanding of programming concepts.
- **Computing Skills**: Comfortable with web browsing and using online tools for learning purposes. May not have programming skills but can navigate online platforms proficiently, including accessing podcasts and video content.

**User Profile 3: Academic Professional**
- **Who**: An academic or researcher seeking to stay updated on the latest research, trends, and discussions within their field of study.
- **Domain Knowledge**: Deep understanding of their specific academic domain, possibly with advanced degrees or professional experience in their field. Likely familiar with TED Talks as a source of thought-provoking discussions.
- **Computing Skills**: Proficient in using online resources for research purposes. May have basic to intermediate programming skills, especially if their field involves data analysis or computational research methods. Comfortable with accessing and processing complex information from various online sources.

## Data Sources

- Youtube Transcript API: to obtain transcripts of a YouTube video based on its link, generated based on user input
- Bard API: to create the summaries from the inputted YouTube video link

- Ted Talks Transcript: https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset 
  -  Contains 19 columns and around 4000 rows of metadata and content information about various TED Talks

- Podcast Transcript Dataset: https://www.kaggle.com/datasets/sentinel3734/skeptoid-podcast-transcripts
  - Contains 9 columns and around 900 rows of information about various podcasts

## User Stories

Some potential stories about users who use the TL;DW application can be found below.

**User Story #1**:
- **Who**: Claire, a high school teacher who is preparing a lesson plan about climate change.
- **Wants**: Claire wants to find other credible videos like podcasts and TED talks to engage her students with unique content.
- **Interaction methods**: Claire accesses the application through a website, inputs a YouTube link that contains similar content to what she wants to teach (Ex: a climate change documentary), and gets recommendations about relevant TED Talks and podcasts related to the documentary
- **Needs**: Claire needs the application to recommend TED Talks and podcasts that offer different perspectives on climate change to widen her students’ perspectives.
- **Skills**: Claire is a high-school teacher and is not well-versed in programming and similarity scores and would prefer a simple user interface.

**User Story #2**:
- **Who**: Mary is a college student who is interested in applying a new machine learning technique to her course project.
- **Wants**: Mary wants to receive a summary of a 3-hour-long lecture to determine if the technique is suitable for her project or not.
- **Interaction methods**: Mary will provide a URL of the video and receive summarized sentences through a web application.
- **Needs**: Mary wants to save time by reviewing new technology without watching lengthy videos.
- **Skills**: Mary is a computer science major and prefers a user-friendly interface.

## Use Cases: 

**Use Case 1: Obtain TED Talk Recommendations about Climate Change**

**Objective**: The system displays related podcasts and TED talks for the video input by the user.

**Interactions**: 
  - User: Inputs the URL for the YouTube video they watched (here about climate change)
  - System: Confirms if the URL is valid and it contains transcript subtitles. If yes, ask users if they wish to see the YouTube video summary or recommendations for TED talks and podcasts. Otherwise, it tells the user that the URL provided doesn’t meet expectations.

  
  - User: Selects that they wish to see recommendations for the TED talks and podcasts
  - System: Asks the user if they want to view TED talk recommendations or podcast recommendations


  - User: Selects TED talk recommendation
  - System: Shows relevant podcasts or TED talks


  - User: Presses the button to limit the time interval of the recommended videos
  - System: shows the filtered recommendations based on time interval input by the user

**Implicit use case**:
- The URL should be working
- The URL should lead to a YouTube video
- The YouTube video should contain subtitles or a transcript

**Use Case 2: Obtain Summary from YouTube through URL**

**Objective**: The system shows a summarization of a YouTube video along with keywords.

**Interactions**: 
  - User: Inputs the URL for the YouTube video they watched
  - System: Confirms if the URL is valid and it contains transcript/ subtitles. If yes, ask users if they wish to see the YouTube video summary or recommendations for TED talks and podcasts. Otherwise, it tells the user that the URL provided doesn’t meet expectations.


  - User: Selects that they wish to see the summary for the YouTube Video
  - System: Passes the relevant YouTube URL to the YouTube Transcript API and returns the transcript.Passes the processed transcript to the summarizer and shows a summary and keywords from the YouTube video to the users. 




