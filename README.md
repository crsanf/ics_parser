This will parse an ICS file and get you the event names and organizer of the events as well as the start and end date/time.

I wrote this back in 2019 so the code is outdated and it has a few bugs. A new version will be posted soon with more features and bug fixes. Overall the code will still work but for parsing lines a .strip() will need to be added to make this properly strip the newline characters! See the Known Bugs section below for a complete list.

Before Running:
- Change the source, and destination file paths.

Running the Script:
- From CLI.PowerShell,Terminal
	- Navigate to where the files and script are
	- Windows: python parse_form.py
	- Mac: python3 prase_form.py

Program Flow:
- Load file from source
- Parse events using the DTSTART and END:VEVENT tag
- Clip the appropriate fields and save the line as a CSV
- Save each created line into the destination file

Features:
- Pulls the fields for Start date/time, End date/time, Organizer, and Summary
- Source file and Destination (Save) locations are in local directory and are hard coded
- Prints a CSV of the resulting parsed data fields that can be used in Excel or another interpreter application

Known Bugs:
- .strip() needed on each line read to properly strip the newline characters. If not added the saved data will be broken as extra newlines are saved alongside the parsed data
- Time is incorrectly parsed as 24 hour but it is instead in Zulu time so the time zones are incorrect. Date is unaffected by this problem.
- Performance might be a problem in larger files or slower machiens since it writes each line after it's found instead of storing all of them in memory prior to writing
