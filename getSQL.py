#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:49:35 2023

@author: joelsommerfeld
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/joelsommerfeld/Desktop/fitnessTracker.db') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Cycling
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['power', 'distance', 'speed', 'cadence'])
#print (df)

import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use("cyberpunk")
plt.plot(df['distance'], df['speed'])
mplcyberpunk.make_lines_glow()
plt.show()


conn.close()

