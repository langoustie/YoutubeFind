The main stages of the project include authenticating the user via OAuth 2.0, retrieving the channels to which the user has subscribed, searching for videos based on channels and keywords, and collecting the user's comments on these videos. The main aim of this project is to create datasets of comments from propaganda bots, trolls and individuals influenced by misinformation on YouTube. The aim is to better understand and identify these groups, while quantifying and tracking the evolution of public opinion on the platform. In particular, this project was used to analyze Russian disinformation campaigns at the start of the war in Ukraine and assess their impact on online discussions.

The script is designed to:

  1) Authenticate the user: Using OAuth 2.0, it authenticates the user and returns a valid service client for further API interactions.
  2) Retrieve Subscribed Channels: For each user channel, it fetches the list of subscriptions (channels the user subscribes to).
  3) Search Videos by Channel and Keywords: The script searches for videos published in the last 30 days on a list of predefined channels, optionally filtered by specific keywords.
  4) Fetch Comments from Videos: Once videos are found, the script fetches the comments for those videos that are authored by the specified user.
  5) Save Comments to a File: All fetched comments are saved to a text file, ensuring duplicate comments are not added.

The YouTube Data API V3 allows developers to interact with YouTube, enabling actions such as retrieving video details, 
channel information, and user comments. You interact with the API using HTTP requests that include various parameters for filtering results.

  Video IDs: Video IDs in YouTube are unique identifiers for each video on the platform. These IDs are part of the video URL (e.g., in https://www.youtube.com/watch?v=VIDEO_ID).
  Channel IDs: A channel ID uniquely identifies a YouTube channel. It is used to query for specific channels, their videos, subscriptions, and more.
  OAuth Authentication: The API uses OAuth 2.0 for authentication, allowing users to authorize the app to access their data.
  You have around 10,000 possible requests per day to the YTB API basic plan. The code allows you to retrieve an average of 200 comments in a single request.

Key API methods used in this script:

  subscriptions().list(): Fetches a list of subscriptions for a specific channel.
  search().list(): Searches for videos across channels, filtering by keywords and publish date.
  commentThreads().list(): Retrieves comments for a specific video.

Dependencies:

  google-auth-oauthlib
  google-api-python-client


