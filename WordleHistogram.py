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
    fname = "AlphaWordle.txt"
text = open(fname)

letters = dict()
pairs = dict()
count = 0
max_letter = ''


for line in text:
    words = line.split()
    for word in words:
        print("New Word") # Loop through each word
        word = re.sub(r'[^\w\s]','', word) # Remove the unnecessary punctuation
        pair = word[:2]
        if pair not in pairs: # Count the occurrence of pairs of letters
            pairs[pair] = 1
            print("First pair")
        else : # If we have seen it before, add another 1 to the previous count
            pairs[pair] = pairs[pair] + 1
            print("Seen this pair before")
        for l in word: # Counting single letter occurrences 
            print("letter") # Loop through each letter
            if l not in letters: # If it is a new letter set it to 1
                letters[l] = 1
                print("First time seeing this letter")
            else : # If we have seen it before, add another 1 to the previous count
                letters[l] = letters[l] + 1
                print("I have seen this letter before")

# Loop to find the most common letter
for ltr in letters :
    if letters[l] > count:
        count = letters[l]
        max_letter = ltr
        print("The letter that appears most is:", l,"with", count, "occurrences")
        
# Probability of each letter occurring
vals = letters.values()
total = sum(vals)

print('Most Common Letter')
prob_dict = {}
for k, v in letters.items():
    prob_dict[k] = (v / total)*100
    print("probabililty of", k, "=", prob_dict[k], "%")
    
print("Probability of Starting Pairs")
pair_prob = {}
for k,v in pairs.items():
    pair_prob[k] = (v/2315)*100
    print("probabililty of", k, "=", pair_prob[k], "%")

        

#import pprint
#pprint.pprint(sorted(prob_dict.items()))
#pprint.pprint(sorted(pair_prob.items()))
#print(sorted(prob_dict.items()))

# Plotting the histogram
plt.bar(list(letters.keys()), letters.values(), color='g')
plt.show()



    

