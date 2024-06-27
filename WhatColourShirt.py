# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:45:02 2024

@author: jsommerfeld
"""

from random import randint
import datetime

# Set inital list of colours
colours = ["green", "black", "grey", "white", "red", "blue", "pink", "purple", "Tuesday's", "Hawaiian"]

# Read in the colour file containing all previous colour options
with open('C:/Users/jsommerfeld/OneDrive - University of Nebraska at Omaha/ThursdayShirts/colours.txt', 'r') as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Get the last 4 entries from the list
last_4_entries = lines[-4:]

# remove newline characters
prev_colours = []
for entry in last_4_entries:
    pc = entry.strip()
    prev_colours.append(pc)

# Pick a colour
possible_colours = [colour for colour in colours if colour not in prev_colours]
num = int(randint(0, 5))

# Find the date of the next Thursday
# Get today's date
today = datetime.date.today()

# Find the weekday of today (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
weekday_today = today.weekday()

# Calculate the number of days until the next Thursday (Thursday = 3)
days_until_thursday = (3 - weekday_today + 7) % 7

# Calculate the date of the next Thursday
next_thursday = today + datetime.timedelta(days=days_until_thursday)

# print("Today's date:", today)
# print("Next Thursday's date:", next_thursday)
email_txt = f"On {next_thursday}, we will be wearing {possible_colours[int(num)]} shirts."
colour_txt = possible_colours[int(num)] + "\n"


# Write the email text to a text file
with open('C:/Users/jsommerfeld/OneDrive - University of Nebraska at Omaha/ThursdayShirts/Outfits/outfit.txt', 'w') as file:
    file.write(email_txt)

# Write the shirt colour to a file so we can keep a track of them
with open('C:/Users/jsommerfeld/OneDrive - University of Nebraska at Omaha/ThursdayShirts/colours.txt', 'a') as file:
    file.write(colour_txt)
