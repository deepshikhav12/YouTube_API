
# Project Goal: 
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Project overview:
```buildoutvfg
1. Uses YouTube API to fetch list of Latest videos of certain search keyword i have used keyword as cricket
2. Stores it in dictionary
3. Displays that dictionary in web page in paginated response
```

This Project is developed using Django framework.

# Result:
After running this django project in your local system the final paginated response will look like this - 

![alt text](https://github.com/deepshikhav12/YouTube_API/blob/main/ytube.png?raw=true)

# Covered Functionalities
- The server continuously calls the YouTube API at regular intervals (currently set at 20 seconds).
- Fetches the latest videos for a predefined search query (currently set as "cricket").
- Stores the video data in a database with appropriate indexes (indexing starts from 1).
- A GET API returns the stored video data in a paginated response, sorted in descending order of published datetime.
- The system is scalable and optimized.
# Key Files Used - 
The key files used in this project are:
- yt_videos/yt/views.py: Contains the code for using the API and extracting data.
- yt_videos/yt/templates/yt/home.html: Contains the code for the web page UI where the final paginated response from the API will be displayed.

# Instructions to start Django Server on Localhost - 

1. Download ZIP file of this repo and extract it in local system.
2. Open the extracted file in Python IDE.
4. Then type the below commands in your terminal for the web server to start.
```buildoutcfg
cd yt_videos
python manage.py runserver
```

# API -
```buildoutcfg
https://www.googleapis.com/youtube/v3/search?part=snippet&q=cricket&maxResults=1&type=video&eventType=completed&order=date&key=AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk

Please note that the API key has a usage limit and might expire after some time. If the result is not displayed, please contact me for a new API key.



