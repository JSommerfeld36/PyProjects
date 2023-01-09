# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:53:23 2023

@author: jsommerfeld
"""

# What os?
# Screen size?
# How many monitors?
# Move teams to main monitor manually - this could maybe be automated
# Run code then use keyboard to bring teams into focus
# Move to random positions every 8 minutes


import pyautogui as p
from time import sleep as t
import datetime as dt


os = input('What OS are you running? (mac/windows)')


# Get the screen size
# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)

if os == 'mac':
    print("we are using a mac")
    t(1)
# Open the program you want
    p.keyDown("command")
    p.keyDown("space")
    t(2)
    p.keyUp("command")
    p.keyUp("space")
    p.typewrite("word")
    p.press("enter")

elif os == 'windows': 
    print("we are using windows")
    p.press('winleft')
    t(2)
    p.typewrite('teams')
    p.press('enter')
    p.keyDown('shift')
    p.keyDown('winleft')
    p.keyDown('left')
    p.keyUp('shift')
    p.keyUp('winleft')
    p.keyUp('left')
    
print("Starting fitness routine")
# print("Move program to main monitor")
# time.sleep(7)

start_time = dt.datetime.now()
minutes_diff = 0

while minutes_diff < 3:
    p.moveTo(300, 300) # Move the mouse to the x, y coordinates 100, 150.
    t(4)
    p.moveTo(300, 800) # Move the mouse to the x, y coordinates 100, 150.
    t(4)
    p.moveTo(500, 300) # Move the mouse to the x, y coordinates 100, 150.
    t(4)
    p.moveTo(500, 800) # Move the mouse to the x, y coordinates 100, 150.
    t(4)
    current_time = dt.datetime.now()
    minutes_diff = (current_time - start_time).total_seconds() / 60.0

