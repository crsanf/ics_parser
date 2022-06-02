#For Regex
import re

"""
Written with Python 3.7.2
3-09-2019 by Christopher Sanfilippo
Tested on Windows 10 Pro x64

To Add Later:
>Parse Repeating of meetings & When They Occur
>Give statistics
"""
###Code Start###

def parse_date(date_string):
    split_date_string = date_string.split(":")
    raw_date = split_date_string[1][:8]
    return format_date_string(raw_date)
        

def parse_time(time_string):
    split_time_string = time_string.split(":")
    raw_time = split_time_string[1][9:15]
    return format_time_string(raw_time)

"""
Old format is YYYYMMDD
New format is MM-DD-YYYY
"""
def format_date_string(raw_date):
    year = raw_date[0:4]
    month = raw_date[4:6]
    day = raw_date[6:8]

    return "" + month + "-" + day + "-" + year

"""
Old format is HHMMSS
New Format is HH:MM:SS AM|PM

"""
def format_time_string(raw_time):
    hour = int(raw_time[0:2])
    minute = raw_time[2:4]
    second = raw_time[4:6]

    if hour > 12:
        time = "PM"
    else:
        time = "AM"

    hour = military_to_12hr(hour)

    return "" + str(hour) + ":" + minute + ":" + second + " " + time

def military_to_12hr(hour):
    subtract = 12

    if hour > subtract:
        return hour - subtract
    else:
        return hour

def get_organizer(organizer_string):
    regex = "(\w+.\w+@me.com)"
    s = re.search(regex,organizer_string)

    if s:
        return s.group(1)
    else:
        return "N/A"

def get_summary(summary_string):
    return summary_string[8:]

#Files to open and save results to
source = "data.txt"
destination = "result.csv"

result_file = open(destination, "w")

#Write CSV header
result_file.write("Start Date,Start Time,End Time,Organizer Email,Summary Name\n")

with open(source) as f:

    for line in f:
        if line.startswith("DTSTART"):
            start_date = parse_date(line)
            start_time = parse_time(line)

        if line.startswith("DTEND"):
            end_date = parse_date(line)
            end_time = parse_time(line)

        if line.startswith("ORGANIZER"):
            organizer_email = get_organizer(line)

        if line.startswith("SUMMARY"):
            summary_name = get_summary(line)

		#Only writes full events
        if line.startswith("END:VEVENT"):
            result_file.write(start_date + "," + start_time + "," 
            + end_time + "," + organizer_email + "," + summary_name)
            
#Close file after writing
result_file.close()
