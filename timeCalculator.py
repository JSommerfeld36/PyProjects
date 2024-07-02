#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:59:48 2024

@author: joelsommerfeld
"""
# Simple time calculator

import re

def split_numbers_letters(s):
    # Use regex to find numbers and letters separately
    match = re.match(r"([0-9]+)([a-zA-Z]+)", s)
    if match:
        return match.groups()
    return None

dist = input("What is the distance? \n")
speed = input("What speed are you travelling at? \n")

# Clean any units off the inputs and convert to numeric 
dist_measure, dist_units = split_numbers_letters(dist)
speed_measure, speed_units = split_numbers_letters(speed)

# speed = distance /time
time = int(dist_measure)/int(speed_measure) * 60

print(f"It would take {time} minutes to travel {dist} at {speed}")