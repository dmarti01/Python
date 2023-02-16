import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
billboard_url = "https://www.billboard.com/charts/hot-100/"
Client_ID = "a6a6a6a3f60f448882596d27adc8fa04"
Client_Secret= "630f68f041ec465795566ec84ed79b8a"
redirect_URI="http://localhost:8888/callback"

#--------------------------------Scraping Billboard --------------------------------------------#
user_date = input("What year would you like to visit? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"{billboard_url}/{user_date}/")
billboard_response = response.text
soup = BeautifulSoup(billboard_response,"html.parser")

song_titles=[song.getText().strip() for song in soup.select(selector="li #title-of-a-story")]

print(song_titles) # Prints the list of songs scraped.

#-------------------Spotify Authentication and token.txt creation ----------------------#

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,
client_secret=Client_Secret,
redirect_uri=redirect_URI,
scope="playlist-modify-private",
show_dialog=True,
cache_path="token.txt"
)
spotify_auth.get_access_token(as_dict=False)
s = spotipy.Spotify(oauth_manager=spotify_auth)
user_id = s.current_user()["id"]
print(user_id)

#--------------------Searching Spotify for the songs----------------------------#
song_uris = []
year = user_date.split("-")[0]
for song in song_titles:
    result = s.search(q=f"track:{song} year:{year}", type="track")
    # print(result) #Prints the result
    try:
        # Handling exception where the song cannot be found. It is skipped in this case.
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris) # You can verify song by visiting https://open.spotify.com/track/URI_ID_GENERATED
#-----------------Creating new private playlist in Spotify--------------------------#
playlist = s.user_playlist_create(user_id,name=f"{user_date} Billboard 100",public=False, description="Musical Time Machine")
#print(playlist)

#---------------- Adding the songs to the playlist----------------------------#
s.playlist_add_items(playlist_id=playlist['id'], items=song_uris)