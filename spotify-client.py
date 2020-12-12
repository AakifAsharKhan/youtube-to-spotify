import os
import tekore as tk


clientId = os.environ.get("SPOTIFY-CLIENT-ID")
clientSecret = os.environ.get("SPOTIFY-CLIENT-SECRET")

# app_token = tk.request_client_token(clientId,clientSecret)
# spotify = tk.Spotify(app_token)

# album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
# print(album.total_tracks)
# for track in album.tracks.items:
#     print(track.name)

redirect_uri = 'http://motherboardtechforum.pythonanywhere.com/'

user_token = tk.prompt_for_user_token(
    clientId,
    clientSecret,
    redirect_uri,
    scope=tk.scope.every
)

spotify.token = user_token

tracks = spotify.current_user_top_tracks(limit=10)
for track in tracks.items:
    print(track.name)