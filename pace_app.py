from flask import Flask, render_template, request, Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2  import SpotifyClientCredentials
import os
from os import getenv
import argparse
import logging
import json
import time
import sys
from requests.exceptions import ReadTimeout
 
#Spotify params
spotify_client_id = os.getenv('SPOTIPY_CLIENT_ID', 'client_id')
spotify_secret = os.getenv('SPOTIPY_CLIENT_SECRET', 'secret')
spotify_redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI', 'redirect_uri')
spotify_api_url = os.getenv('api_url', 'api_url')
 
#auth_manager = SpotifyClientCredentials()


    

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
    scope = "playlist-modify-public user-library-read user-top-read user-read-recently-played" 
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), requests_timeout=10, retries=10)
    sp.trace = True
    user_id = sp.me()['id']
    playlist_items=[]
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
    margin_of_error=bpm*0.3
    #parser = argparse.ArgumentParser(description='Creates a playlist for user')
    
    #parser.add_argument('-p', '--playlist', required=False, default='Cadence Playlist', help='Name of Playlist')
    #parser.add_argument('-d', '--description', required=False, default='', help='Description of Playlist')
    #args = parser.parse_args()
    
    #make playlist
    
    playlist_name="Cadenza Playlist"
    playlist_description="Made for you by the Cadenza App, to run {distance}km in {h}h{m}m{s}s. Keep to the beat!".format(
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

    tracks_added_to_list=0

    saved_offset=0
    saved_track_count=0
    keep_counting_saved=True
    while keep_counting_saved==True:
        library = sp.current_user_saved_tracks(limit=50, offset=saved_offset, market=None) 
        for item in (library['items']):
            track_id = item['track']['id']
            track = sp.track(track_id, market=None)
            features = sp.audio_features(track_id)
            for feature in features:
                analysis= sp._get(feature['analysis_url'])
                tempo=analysis['track']['tempo']
                track_duration=track['duration_ms']
                track_name=track['name']
                saved_track_count=saved_track_count+1
                tempo=int(tempo)
                track_duration=int(track_duration)
            if playlist_length<desired_time_in_seconds and ((tempo<(bpm+margin_of_error) and tempo>(bpm-margin_of_error))or (0.5*tempo<(bpm+margin_of_error) and 0.5*tempo>(bpm-margin_of_error)) or (2*tempo<(bpm+margin_of_error) and 2*tempo>(bpm-margin_of_error))):
                playlist_items.append(track_id)
                playlist_length=playlist_length+(track_duration)
                tracks_added_to_list=tracks_added_to_list+1
            if saved_track_count%50 == 0 and tracks_added_to_list<101:
                keep_counting_saved=True
            else:
                keep_counting_saved=False
        saved_offset=saved_offset+50
        print("Keep counting? ", keep_counting_saved)
        print("Saved items checked: ", saved_track_count)   
        print("Tracks added to list so far: ", tracks_added_to_list)

    tops_offset=0
    tops_track_count=0
    keep_counting_tops=True
    while keep_counting_tops==True and tracks_added_to_list<101:
        tops = sp.current_user_top_tracks(limit=20, offset=tops_offset, time_range='medium_term')
        for track in (tops['tracks']):
            track_id = track['id']
            track = sp.track(track_id, market=None)
            features = sp.audio_features(track_id)
            for feature in features:
                analysis= sp._get(feature['analysis_url'])
                tempo=analysis['track']['tempo']
                track_duration=track['duration_ms']
                track_name=track['name']
                tops_track_count=tops_track_count+1
                tempo=int(tempo)
                track_duration=int(track_duration)
            if playlist_length<desired_time_in_seconds and ((tempo<(bpm+margin_of_error) and tempo>(bpm-margin_of_error))or (0.5*tempo<(bpm+margin_of_error) and 0.5*tempo>(bpm-margin_of_error)) or (2*tempo<(bpm+margin_of_error) and 2*tempo>(bpm-margin_of_error))):
                playlist_items.append(track_id)
                playlist_length=playlist_length+(track_duration)
                tracks_added_to_list=tracks_added_to_list+1
            if tops_track_count%20 == 0 and tracks_added_to_list<101:
                keep_counting_tops=True
            else:
                keep_counting_tops=False
        tops_offset=tops_offset+20
        print("Keep counting? ", keep_counting_tops)
        print("Saved items checked: ", tops_track_count)   
        print("Tracks added to list so far: ", tracks_added_to_list)

    
    #recent_offset=0
    recent_track_count=0
    #keep_counting_recent=True
    while tracks_added_to_list<101:
        recents = sp.current_user_recently_played(limit=100, after=None, before=None) 
        for item in (recents['items']):
            track_id = item['track']['id']
            track = sp.track(track_id, market=None)
            features = sp.audio_features(track_id)
            for feature in features:
                analysis= sp._get(feature['analysis_url'])
                tempo=analysis['track']['tempo']
                track_duration=track['duration_ms']
                track_name=track['name']
                recent_track_count=recent_track_count+1
                tempo=int(tempo)
                track_duration=int(track_duration)
            if playlist_length<desired_time_in_seconds and ((tempo<(bpm+margin_of_error) and tempo>(bpm-margin_of_error))or (0.5*tempo<(bpm+margin_of_error) and 0.5*tempo>(bpm-margin_of_error)) or (2*tempo<(bpm+margin_of_error) and 2*tempo>(bpm-margin_of_error))):
                playlist_items.append(track_id)
                playlist_length=playlist_length+(track_duration)
                tracks_added_to_list=tracks_added_to_list+1
            if recent_track_count%50 == 0 and tracks_added_to_list<101:
                keep_counting_recent=True
            else:
                keep_counting_recent=False
        recent_offset=recent_offset+50
        print("Keep counting? ", keep_counting_recent)
        print("Saved items checked: ", recent_track_count)   
        print("Tracks added to list so far: ", tracks_added_to_list)

    new_playlist= sp.user_playlist_create(user, name, public=True, collaborative=False, description=description)
    new_playlist_id=new_playlist['id']
    print("New playlist: ", new_playlist_id)
    
    playlist_url=new_playlist['external_urls']['spotify']
    playlist_message = "Here's your playlist!"

    playlist_items_list_out=playlist_items
    sp.playlist_add_items(new_playlist_id, playlist_items_list_out, position=None)    
    
    playlist_length_in_secs=playlist_length/1000
    if playlist_length_in_secs<desired_time_in_seconds:
        playlist_message = "On no! There is not enough music in your library to cover the whole run. You may have to put this playlist on repeat!"
    else:
        playlist_message = "What a great playlist - you have very good taste!"
    
    overall_track_count=saved_track_count

    playlist_length_in_mins=playlist_length_in_secs/60
    print("Playlist length in minutes: ", playlist_length_in_mins)
    print(overall_track_count, "tracks checked")
    return render_template("results.html", bpm=bpm, stride=stride_in_metres, km=form_data['desired_distance'], hours=form_data['desired_time_hours'], mins=form_data['desired_time_minutes'], seconds=form_data['desired_time_seconds'], new_playlist_id=new_playlist['id'], playlist_message=playlist_message)

   # return sp.playlist_add_items(playlist_id, items)

#debug
if __name__ == '__main__':
    app.run(app.run(debug=True)) #runs the app. the debug part - unlocks debugging feature
