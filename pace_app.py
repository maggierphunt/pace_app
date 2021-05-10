from flask import Flask, render_template, request, Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2  import SpotifyClientCredentials
import os
from os import getenv
import argparse
import logging
 
#Spotify params
spotify_client_id = os.getenv('SPOTIPY_CLIENT_ID', 'client_id')
spotify_secret = os.getenv('SPOTIPY_CLIENT_SECRET', 'secret')
spotify_redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI', 'redirect_uri')
spotify_api_url = os.getenv('api_url', 'api_url')
 
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
items=[]
 
logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')
 



#logger = logging.getLogger('examples.create_playlist')
#logging.basicConfig(level='DEBUG')


###################
app = Flask("pace_app") #making an app
       
#About
@app.route("/about", methods=["POST", "GET"])    
def about_page():
        return render_template("about.html")

#Homepage
@app.route("/", methods=["POST", "GET"])
def home_page():
        return render_template("index.html")

#Results
@app.route("/results", methods=["POST", "GET"])
def results():
    form_data = request.form
#raw_input
    pace_minutes1 = int(form_data['pace_minutes1'])
    pace_seconds1 = int(form_data['pace_seconds1'])
    cadence1 = int(form_data['cadence1'])

    pace_minutes2 = int(form_data['pace_minutes2'])
    pace_seconds2 = int(form_data['pace_seconds2'])
    cadence2 = int(form_data['cadence2'])

    pace_minutes3 = int(form_data['pace_minutes3'])
    pace_seconds3 = int(form_data['pace_seconds3'])
    cadence3 = int(form_data['cadence3'])

    desired_distance = int(form_data['desired_distance'])
    desired_time_hours = int(form_data['desired_time_hours'])
    desired_time_minutes = int(form_data['desired_time_minutes'])
    desired_time_seconds = int(form_data['desired_time_seconds'])
#total time for 1km in seconds
    km_pace_1 = (pace_minutes1 * 60) + pace_seconds1
    km_pace_2 = (pace_minutes2 * 60) + pace_seconds2
    km_pace_3 = (pace_minutes3 * 60) + pace_seconds3
#total distance covered in a minute
    distance_in_a_minute_1 = 1/km_pace_1*60
    distance_in_a_minute_2 = 1/km_pace_2*60
    distance_in_a_minute_3 = 1/km_pace_3*60
#steplength
    step_length_1 = distance_in_a_minute_1 / cadence1
    step_length_2 = distance_in_a_minute_2 / cadence2
    step_length_3 = distance_in_a_minute_3 / cadence3
    average_step_length = (step_length_1+step_length_2+step_length_3)/3
    print (average_step_length)
    stride_in_metres = round(average_step_length*1000,2)
#desired result
    number_of_steps_to_do = desired_distance / average_step_length
    desired_time_in_seconds = (desired_time_hours*60*60) + (desired_time_minutes * 60) + desired_time_seconds
    seconds_pace = number_of_steps_to_do / desired_time_in_seconds
    minute_pace = seconds_pace * 60
    bpm = round(minute_pace)
    print (bpm)

    #parser = argparse.ArgumentParser(description='Creates a playlist for user')
    
    #parser.add_argument('-p', '--playlist', required=False, default='Cadence Playlist', help='Name of Playlist')
    #parser.add_argument('-d', '--description', required=False, default='', help='Description of Playlist')
    #args = parser.parse_args()
    
    #make playlist
    scope = "playlist-modify-public user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    playlist_name="Cadence Playlist"
    playlist_description="Made for you by the Cadence App, to run {distance}km in {h}h{m}m{s}s. Keep to the beat!".format(
        distance = desired_distance,
        h = desired_time_hours,
        m = desired_time_minutes,
        s = desired_time_seconds
        )
    
    user=user_id
    name=playlist_name
    description=playlist_description
    playlist_owner_id=user_id
    playlist_length=0

    new_playlist= sp.user_playlist_create(user, name, public=True, collaborative=False, description=description)
    playlist_id=new_playlist['id']
    playlist_url=new_playlist['external_urls']['spotify']
    
    
    def list_tracks():
        library = sp.current_user_saved_tracks()
        for idx, item in enumerate(library['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'], track['tempo'])
            margin_of_error=bpm*0.1
            if playlist_length<desired_time_in_seconds and item['tempo']<(bpm+margin_of_error) and item['tempo']>(bpm-margin_of_error):
                items_list.append(idx)
                playlist_length=playlist_length+(track[duration_ms]*1000)
        items_list_out=items_list
        print (list_tracks)
        return list_tracks()
    
    playlist_message = "Here's your playlist!"
    def fill_playlist():
        items_list_out=items_list
        sp.playlist_add_items(playlist_id, items_list_out, position=None)
        if playlist_length<desired_time_in_seconds:
            playlist_message = "On no! There is not enough music in your library to cover the whole run. You may have to put this playlist on repeat!"
        else:
            playlist_message = "What a great playlist - you have very good taste!"
        print("Playlist length in seconds: ", playlist_length)
        return fill_playlist()
    
    #list_tracks()
    #fill_playlist()
    return render_template("results.html", bpm=bpm, stride=stride_in_metres, km=form_data['desired_distance'], hours=form_data['desired_time_hours'], mins=form_data['desired_time_minutes'], seconds=form_data['desired_time_seconds'], playlist_id=new_playlist['id'], playlist_message=playlist_message)

   # return sp.playlist_add_items(playlist_id, items)

#debug
if __name__ == '__main__':
<<<<<<< HEAD
    app.run(app.run(debug=True)) #runs the app. the debug part - unlocks debugging feature
=======
    app.run(app.run(debug=True)) #runs the app. the debug part - unlocks debugging feature
>>>>>>> 48263c14e6db9a6c3c6463d1cbf34ef6d0711c4f
