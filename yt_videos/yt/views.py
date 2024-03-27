from django.shortcuts import render

import requests
import json



class YTData:
    def __init__(self, api_key, query): 
        self.api_key = api_key
        self.query = query
        self.next_page_token = None
        self.data = dict()  
        self.data['Video List'] = []
        self.count = 1

   
    def get_channel_stats_page1(self):
        
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={self.query}&maxResults=100&type=video&eventType=completed&order=date&key={self.api_key}'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            
            n = data['pageInfo']['resultsPerPage']
            
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                channel = data['items'][i]['snippet']['channelTitle']
                
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image, "channel":channel})
                self.count += 1

        except:
            data = None

    
    def get_channel_stats_pagen(self):
        
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&pageToken={self.next_page_token}&maxResults=100&q={self.query}&type=video&eventType=completed&order=date&key={self.api_key}'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            
            n = data['pageInfo']['resultsPerPage']
            
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                channel = data['items'][i]['snippet']['channelTitle']
                
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image, "channel":channel})
                self.count += 1

        except:
            data = None

    
    def return_data(self):
        return self.data



def display_string(request):
    
    API_Key = ["AIzaSyAkLWQGo-rHoHAVTpz8M_c_kQ2Hap99iw0"]
    
    query = "cricket"
    
    current_api=""
    for i in range(len(API_Key)):
        if i == len(API_Key):
            
            print("All API Keys are Exhausted!\nTry Again Tomorrow!")
            break
        
        
        
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=100&type=video&eventType=completed&order=date&key={API_Key[i]}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        
        if "error" in data:
            pass
        else:
            
            print("API Key", i + 1, "is used!")
            api = API_Key[i]
            current_api=api
    
    yt = YTData(current_api, query)
    yt.get_channel_stats_page1()
    yt.get_channel_stats_pagen()
    
    dictionary_data = yt.return_data()
    dictionary_data = dictionary_data['Video List']
    
    context = {'data': dictionary_data}
    return render(request, 'yt/home.html', context)
