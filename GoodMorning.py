# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 08:33:13 2023

@author: jsommerfeld
"""

# Open all the apps in the morning

from AppOpener import open

import pyautogui as p
from time import sleep as t
import datetime as dt

open("Outlook") # Opens Outlook
open("Microsoft Teams")

t(12) # pause while Outlook opens and emails load

# Move cursor to the calendar tab and click
p.moveTo(80, 1330)
p.mouseDown()
p.mouseUp()
t(1)
p.mouseDown()
p.mouseUp()
t(1)
