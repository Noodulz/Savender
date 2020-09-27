import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from termcolor import colored, cprint
import time
import config

clientID = config.spotify_client
clientSecret = config.spotify_secret

creds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=creds)

def search_track(inputer):
    artist_name = []
    track_name = []

    for i in range(0, 20, 5):
        results = sp.search(q=inputer, type='track', limit = 5, offset=i)
        for i, t in enumerate(results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
    
    result = track_name[0] + " by " + artist_name[0]
    return result

def get_track_id(inputer):
    track_id = []
    for i in range(0, 5, 5):
        results = sp.search(q=inputer, type='track', limit=5, offset=i)
        for i, t in enumerate(results['tracks']['items']):
            track_id.append(t['id'])
    id = [track_id[0]]
    return id

def get_genre_list():
    for i in sp.recommendation_genre_seeds()['genres']:
        print(i)

def get_artist_id(inputer):
    artist_id = []
    for i in range(0, 5, 5):
        results = sp.search(q=inputer, type ='track', limit=5, offset=i)
        for i, t in enumerate(results['tracks']['items']):
            artist_id.append(t['artists'][0]['id'])
    id = [artist_id[0]]
    return id

def get_genres(inputer):
    artist_genre = []
    result = sp.search(inputer)
    track = result['tracks']['items'][0]
    artist = sp.artist(track['artists'][0]['external_urls']['spotify'])
    artist = artist["genres"]
    for i in range(0, len(artist)):
        if "indie" in artist[i]:
            artist[i] = "indie"
    return artist

def get_recommendations(artist, genres, tracks):
    artists = []
    tracks = []
    fullQuery = []
    n = 0
    results = sp.recommendations(seed_artists=artist, seed_genres=genres, seed_tracks=tracks, limit=5)
    for t in results['tracks']:
        artists.append(t['artists'][0]['name'])
        tracks.append(t['name'])
        stringQuery = tracks[n] + " by " + artists[n]
        fullQuery.append(stringQuery)
        n += 1
    n = 0
    return fullQuery

def main():
    stringer = "\nEnter a song you like: "
    print(colored(stringer, 'green'))
    query = input()
    aID = get_artist_id(query)
    genre = get_genres(query)
    tID = get_track_id(query)
    time.sleep(0.5)
    print(colored("\nFound! Try listening to: ", 'red'))
    for i in get_recommendations(aID, genre, tID):
        print(colored(i, 'cyan'))
    query = input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()

