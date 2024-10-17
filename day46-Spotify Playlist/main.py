import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "______YOUR_SPOTIFY_CLIENT_ID_____"
SPOTIFY_CLIENT_SECRET = "______YOUR_SPOTIFY_CLIENT_SECRET_____"

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = f"http://www.billboard.com/charts/hot-100/{date}"
res = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(res.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Rudolf",
    )
)

user_id = sp.current_user()["id"]
print(f"user_id:{user_id}")

# Searching Spotify for songs by title
song_urls = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_urls.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        continue


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)