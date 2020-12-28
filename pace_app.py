
def calculate_bpm(bpm):
    bpm = 0
#raw_input
    pace_minutes1 = input("What was your km pace for example run 1 (minutes)?")
    pace_seconds1 = input("What was your km pace for example run 1 (seconds)?")
    cadence1 = input("Whats was your cadence in example run 1?")
        
    pace_minutes2 = input("What was your km pace for example run 2 (minutes)?")
    pace_seconds2 = input("What was your km pace for example run 2 (seconds)?")
    cadence2 = input("Whats was your cadence in example run 2?")

    pace_minutes3 = input("What was your km pace for example run 3 (minutes)?")
    pace_seconds3 = input("What was your km pace for example run 3 (seconds)?")
    cadence3 = input("Whats was your cadence in example run 3?")

    desired_distance = input("What is the distance you are training for (km)?")
    desired_time_hours = input("How much time would you like to run it in (hours)?")
    desired_time_minutes = input("How much time would you like to run it in (minutes)?")
    desired_time_seconds = input("How much time would you like to run it in (seconds)?")

#converting to ints
#    int(pace_minutes1)
#    int(pace_minutes2)
#    int(pace_minutes3)
#    int(pace_seconds1)
#    int(pace_seconds3)
#    int(pace_seconds2)
#    int(cadence1)
#    int(cadence2)
#    int(cadence3)
#    int(desired_distance)
#    int(desired_time_hours)
#    int(desired_time_minutes)
#    int(desired_time_seconds)

#total time for 1km in seconds
    km_pace_1 = (pace_minutes1 * 60) + pace_seconds1
    return (km_pace_1)
    km_pace_2 = (pace_minutes2 * 60) + pace_seconds2
    return (km_pace_2)
    km_pace_3 = (pace_minutes3 * 60) + pace_seconds3
    return (km_pace_3)

#total distance covered in a minute
    distance_in_a_minute_1 = 60000 / km_pace_1
    return (distance_in_a_minute_1)
    distance_in_a_minute_2 = 60000 / km_pace_2
    return (distance_in_a_minute_2)
    distance_in_a_minute_3 = 60000 / km_pace_3
    return (distance_in_a_minute_3)

#steplength
    step_length_1 = distance_in_a_minute_1 / cadence1
    return step_length_1
    step_length_2 = distance_in_a_minute_2 / cadence2
    return step_length_2
    step_length_3 = distance_in_a_minute_3 / cadence3
    return step_length_3

    average_step_length = (step_length_1+step_length_2+step_length_3)/3
    return (average_step_length)
    print (average_step_length)

#desired result
    number_of_steps_to_do = desired_distance / average_step_length2
    desired_time_in_seconds = (desired_time_hours*60*60) + (desired_time_minutes * 60) + desired_time_seconds
    seconds_pace = number_of_steps_to_do / desired_time_in_seconds
    minute_pace = seconds_pace * 60
    bpm = minute_pace
    return (bpm)

print (bpm " BPM")

calculate_bpm()
