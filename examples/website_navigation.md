- Refer the [README](https://github.com/JoobeeJung/TLDW/blob/main/examples/README.md) file for details on how to launch the wesbite locally.

## Navigation ##
 - Once the website launches, we are able to view the homepage asking for a dialogue box to enter the URL for the youtube video.

 ![Home Page screenshot](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/home_page.png)

 - If the video is a valid YouTube video, the website will commence the summarization process. Otherwise, it will display a message to the user indicating that the provided URL is not a valid YouTube video.

![Youtube video being fed to the summarizer](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/input_url.png)

- Once the summarizer completes its operation successfully, the system informs the user that the process of summarization and extraction of keywords was successful. It then displays the summary as well as top 10 keywords identified by Gemini for the input video.

![Summary shown by the website](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/summary.png)

![Keywords shown by the website](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/keywords.png)

- After completing the aforementioned process, the website provides the user with an option to choose between Ted Talks or Podcasts, similar to the video provided by the user at the beginning. To recommend similar content, we've incorporated three recommendation methods and provide the user three recommended vidoes, based on the top three similarity scores:
 - [SBERT recommender](https://www.sbert.net/)
 - [MiniLM recommender](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
 - [TF-IDF recommender](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

Below is a screenshot demonstrating the use of SBERT to obtain the top three recommendations for Ted Talks. Users can select a video and access the URL for the recommended video, along with viewing the generated similarity score.

![SBERT Tedtalks](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/tedtalks_recommendation.png)

Below is a screenshot demonstrating the use of TF-IDF to obtain the top three recommendations for Podcasts. Users can select a video and access the URL for the recommended video, along with viewing the generated similarity score.

![tf-idf posdcasts](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/podcasts_recommendations.png)

- Once the user selects the recommended video from the various options provided by us, they can interact with the chatbot provided at the end of the website to ask any related questions.

![chat-bot](https://github.com/JoobeeJung/TLDW/blob/main/examples/images/chat_bot.png)





  
