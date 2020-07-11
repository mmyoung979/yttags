# Python imports
import requests
import json

# 3rd party imports
from googleapiclient.discovery import build

# Project imports
try:
    from config.settings.production import YOUTUBE_KEY
except ImportError as e:
    from config.settings.local import YOUTUBE_KEY

# Global variables
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


# Get video data from YouTube API
def get_video_data(video_id):
    params = 'fields=items(snippet(title, thumbnails, tags))&part=snippet'
    url = 'https://www.googleapis.com/youtube/v3/videos?key=%s&%s&id=%s' % (YOUTUBE_KEY, params, video_id)
    r = requests.get(url)
    video = json.loads(r.content)['items'][0]['snippet']
    data = {
        'title': video['title'],
        'thumbnail': video['thumbnails']['medium']['url'],
    }

    try:
        data['tags'] = video['tags']
    except KeyError:
        data['tags'] = []

    return data


# Search YouTube videos
def youtube_search(search, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_KEY)

    # Call the search.list method to retrieve results matching the specified query term
    search_response = youtube.search().list(
        q=search,
        part="id,snippet",
        maxResults=max_results,
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of matching videos
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))

    return videos
