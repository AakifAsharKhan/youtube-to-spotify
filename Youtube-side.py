import os
from googleapiclient.discovery import build


api_key = os.environ.get('YOUTUBE-API-KEY')

li = list()

service = build('youtube', 'v3', developerKey=api_key)

request = service.playlistItems().list(
    part='contentDetails',
    playlistId="PLvczmdAAtKHtY2Cz_Gd8n4Ry9dO7DtgTv",
    maxResults=50
)



response = request.execute()


for i in response['items']:
    temp = i['contentDetails']['videoId']
    name_request = service.videos().list(
        part='id,snippet',
        id=temp,
        
    )
    name_response = name_request.execute()
    temp = name_response['items'][0]['snippet']['title']
    li.append(temp)

while response:
    request = service.playlistItems().list_next(request,response)
    try:
        response = request.execute()
        for i in response['items']:
            temp = i['contentDetails']['videoId']
            name_request = service.videos().list(
            part='id,snippet',
            id=temp, 
            )
            name_response = name_request.execute()
            temp = name_response['items'][0]['snippet']['title']
            li.append(temp)
    except:
        print("reached Limit")
        break

with open(r'playlist.text','w+') as file:
    for i in li:
        file.write(i)