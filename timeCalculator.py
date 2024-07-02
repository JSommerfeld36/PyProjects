#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:59:48 2024

@author: joelsommerfeld
"""
# Simple time calculator

import re

purple_color_code = "\033[35m"
green_color_code = "\033[32m"
reset_color_code = "\033[0m"


def split_numbers_letters(s):
    # Use regex to find numbers and letters separately
    match = re.match(r"([0-9]+)([a-zA-Z]+)", s)
    if match:
        return match.groups()
    return None

dist = input(f"{purple_color_code}What is the distance? \n {reset_color_code}")
speed = input(f"{purple_color_code}What speed are you travelling at? \n {reset_color_code}")

# Clean any units off the inputs and convert to numeric 
dist_measure, dist_units = split_numbers_letters(dist)
speed_measure, speed_units = split_numbers_letters(speed)

# speed = distance /time
time = int(dist_measure)/int(speed_measure) * 60

time = round(float(time), 2)

print(f"{green_color_code}It would take {time} minutes to travel {dist} at {speed}{reset_color_code}")