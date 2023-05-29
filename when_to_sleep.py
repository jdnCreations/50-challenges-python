from fractions import Fraction

# (alarm time, sleep duration)
# hours in day - sleep duration + alarm time

hours_in_day = 24
day_in_minutes = hours_in_day * 60

def bed_times(*times):
    bed_times_list = []
    for i in range(len(times)):
        alarm_time = times[i][0]
        sleep_duration = times[i][1]

        # split on :
        alarm_hrs, alarm_mins = alarm_time.split(":")
        sleep_hrs, sleep_mins = sleep_duration.split(":")

        # convert to minutes
        alarm_time_in_mins = int(alarm_hrs) * 60 + int(alarm_mins)
        sleep_time_in_mins = int(sleep_hrs) * 60 + int(sleep_mins)

        bed_time = (day_in_minutes - sleep_time_in_mins + alarm_time_in_mins)
        bed_time = bed_time / 60

        bed_time = str(bed_time)

        bed_hrs, bed_mins = bed_time.split(".")

        if len(bed_hrs) == 1:
            bed_hrs = "0" + bed_hrs
        if len(bed_mins) == 1:
            bed_mins = bed_mins + "0"

        bed_mins = (Fraction(bed_mins) * 60) / 100

        if bed_hrs == 24:
            bed_hrs = 00

        bed_times_list.append(f'{bed_hrs}:{bed_mins}')
    return bed_times_list


print(bed_times(["07:50", "07:50"]))
print(bed_times(['06:15', '10:00'], ['08:00', '10:00'], ['09:30', '10:00']))
# doesn't work yet
# print(bed_times(['05:45', '04:00'], ['07:10', '04:30']))

