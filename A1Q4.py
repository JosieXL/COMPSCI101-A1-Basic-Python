"""
Name: Xiaolin Li (Josie)
Username: xli556
ID number: 455398598
Description: This program is used to calculate the final time (in hours, minutes and seconds) when given a start time and a time to add.
"""
line = "=" * 35
blanks = " " * 2

start_time = "23:32:59"
first_colon = start_time.find(":")
last_colon = start_time.rfind(":")
hours = int(start_time[:first_colon])
minutes = int(start_time[first_colon + 1 : last_colon])
seconds = int(start_time[last_colon + 1:])

time_to_add = "00:27:01"
time_to_add_hours = int(time_to_add[:time_to_add.find(":")])
time_to_add_minutes = int(time_to_add[time_to_add.find(":") + 1 : time_to_add.rfind(":")])
time_to_add_seconds = int(time_to_add[time_to_add.rfind(":") +1:])
hours_add_seconds = time_to_add_hours * 60 * 60 #hours convert to seconds
minutes_add_seconds = time_to_add_minutes * 60 #minutes convert to seconds
seconds_to_add = hours_add_seconds + minutes_add_seconds + time_to_add_seconds 

end_time_seconds_within_60 = str((seconds + time_to_add_seconds) % 60)
end_time_seconds = "00" + end_time_seconds_within_60
end_time_seconds_above_60 = (seconds + time_to_add_seconds) // 60
end_time_minutes_within_60 = str((minutes + time_to_add_minutes + end_time_seconds_above_60) % 60)
end_time_minutes = "00" + end_time_minutes_within_60
end_time_minutes_above_60 = (minutes + time_to_add_minutes + end_time_seconds_above_60) // 60
end_time_hours_within_24 = str((hours + time_to_add_hours + end_time_minutes_above_60) % 24)
end_time_hours = "00" + end_time_hours_within_24

print(line)
print(blanks + "Start time: " + start_time)
print(blanks + "Seconds to add: " + str(seconds_to_add) + " (" + time_to_add + ")")
print(blanks + "End time: " + end_time_hours[-2:] + ":" + end_time_minutes[-2:] + ":" + end_time_seconds[-2:])
print(line)
