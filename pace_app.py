
from flask import Flask, render_template, request, Response

app = Flask("pace_app") #making an app

#About
@app.route("/about")  
def about_page():
        return render_template("about.html")

#Homepage
@app.route("/")
def calculate_bpm():
    return render_template("index.html")
#raw_input
    pace_minutes1 = int(input("What was your km pace for example run 1 (minutes)?"))
    pace_seconds1 = int(input("What was your km pace for example run 1 (seconds)?"))
    cadence1 = int(input("Whats was your cadence in example run 1?"))

    pace_minutes2 = int(input("What was your km pace for example run 2 (minutes)?"))
    pace_seconds2 = int(input("What was your km pace for example run 2 (seconds)?"))
    cadence2 = int(input("Whats was your cadence in example run 2?"))

    pace_minutes3 = int(input("What was your km pace for example run 3 (minutes)?"))
    pace_seconds3 = int(input("What was your km pace for example run 3 (seconds)?"))
    cadence3 = int(input("Whats was your cadence in example run 3?"))

    desired_distance = int(input("What is the distance you are training for (km)?"))
    desired_time_hours = int(input("How much time would you like to run it in (hours)?"))
    desired_time_minutes = int(input("How much time would you like to run it in (minutes)?"))
    desired_time_seconds = int(input("How much time would you like to run it in (seconds)?"))
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
    print (average_step_length, "average step length")
#desired result
    number_of_steps_to_do = desired_distance / average_step_length
    desired_time_in_seconds = (desired_time_hours*60*60) + (desired_time_minutes * 60) + desired_time_seconds
    seconds_pace = number_of_steps_to_do / desired_time_in_seconds
    minute_pace = seconds_pace * 60
    bpm = round(minute_pace)
    print (bpm, "bpm")


#Results
@app.route("/results")  
def results():
        return render_template("results.html")

#debug
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature
