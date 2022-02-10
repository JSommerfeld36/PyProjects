#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:50:26 2022

@author: joelsommerfeld
"""

# Wordle Histogram
import re
import matplotlib.pyplot as plt

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "WordleList.txt"
text = open(fname)

letters = dict()
count = 0
max_letter = ''


for line in text:
    words = line.split()
    for word in words:
        print("New Word") # Loop through each word
        word = re.sub(r'[^\w\s]','', word) # Remove the unnecessary punctuation
        for l in word: 
            print(l) # Loop through each letter
            if l not in letters: # If it is a new letter set it to 1
                letters[l] = 1
                print("this is new")
            else : # If we have seen it before, add another 1 to the previous count
                letters[l] = letters[l] + 1
                print("seen it before")

# Loop to find the most common letter
for ltr in letters :
    if letters[l] > count:
        count = letters[l]
        max_letter = ltr
        print("The letter that appears most is:", l,"with", count, "occurrences")
        
# Probability of each letter occurring
vals = letters.values()
total = sum(vals)

prob_dict = {}
for k, v in letters.items():
    prob_dict[k] = (v / total)*100
    print("probabililty of", k, "=", prob_dict[k], "%")

import pprint
pprint.pprint(sorted(prob_dict.items()))
#print(sorted(prob_dict.items()))

# Plotting the histogram
plt.bar(list(letters.keys()), letters.values(), color='g')
plt.show()



    

