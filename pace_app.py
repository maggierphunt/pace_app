
from flask import Flask, render_template, request, Response

app = Flask("pace_app") #making an app

#About
@app.route("/about")  
def about_page():
        return render_template("about.html")

#Homepage
@app.route("/")
def home_page():
        return render_template("index.html")

#Results
@app.route("/results", methods=["GET", "POST"])  
def calculate_bpm():
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
    print (average_step_length, "average step length")
#desired result
    number_of_steps_to_do = desired_distance / average_step_length
    desired_time_in_seconds = (desired_time_hours*60*60) + (desired_time_minutes * 60) + desired_time_seconds
    seconds_pace = number_of_steps_to_do / desired_time_in_seconds
    minute_pace = seconds_pace * 60
    bpm = round(minute_pace)
    print (bpm, "bpm")

    return render_template("results.html", bpm)

#debug
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature
