#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:50:26 2022

@author: joelsommerfeld
"""

# Wordle Histogram
import matplotlib.pyplot as plt

# fname = input("Enter file name: ")
# if len(fname) < 1:
fname = "AlphaWordle.txt"
text = open(fname)


# Single Letters
letters = dict()
first_letters = dict()
second_letters = dict()
third_letters = dict()
fourth_letters = dict()
fifth_letters = dict()

# Pairs
first_pairs = dict()
last_pairs = dict()
count = 0
max_letter = ''

for line in text:
    words = line.split()
    for n in range(len(words)):
        print("New Word") # Loop through each word
        word = words[n]
        
# First Letter
        first_letter = word[0]
        if first_letter not in first_letters: 
            first_letters[first_letter] = 1
            print("new first letter")
        else : # If we have seen it before, add another 1 to the previous count
            first_letters[first_letter] = first_letters[first_letter] + 1
            print("Seen this letter first before")

# Second Letter
        second_letter = word[1]
        if second_letter not in second_letters: 
            second_letters[second_letter] = 1
            print("new second letter")
        else : # If we have seen it before, add another 1 to the previous count
            second_letters[second_letter] = second_letters[second_letter] + 1
            print("Seen this letter second before")
            
# Third Letter
        third_letter = word[2]
        if third_letter not in third_letters: 
            third_letters[third_letter] = 1
            print("new third letter")
        else : # If we have seen it before, add another 1 to the previous count
            third_letters[third_letter] = third_letters[third_letter] + 1
            print("Seen this letter third before")
            
# Fourth Letter
        fourth_letter = word[3]
        if fourth_letter not in fourth_letters: 
            fourth_letters[fourth_letter] = 1
            print("new fourth letter")
        else : # If we have seen it before, add another 1 to the previous count
            fourth_letters[fourth_letter] = fourth_letters[fourth_letter] + 1
            print("Seen this letter fourth before")
            
# Fifth Letter
        fifth_letter = word[4]
        if fifth_letter not in fifth_letters: 
            fifth_letters[fifth_letter] = 1
            print("new fifth letter")
        else : # If we have seen it before, add another 1 to the previous count
            fifth_letters[fifth_letter] = fifth_letters[fifth_letter] + 1
            print("Seen this letter fifth before")

        
        # Get the occurrence of pairs of letters at the start of the words
        first_pair = word[:2]
        if first_pair not in first_pairs: 
            first_pairs[first_pair] = 1
            print("new first pair")
        else : # If we have seen it before, add another 1 to the previous count
            first_pairs[first_pair] = first_pairs[first_pair] + 1
            print("Seen this first pair before")
            
        # Get the occurrence of pairs of letters at the end of the words
        last_pair = word[3:]
        if last_pair not in last_pairs: 
            last_pairs[last_pair] = 1
            print("new last pair")
        else : # If we have seen it before, add another 1 to the previous count
            last_pairs[last_pair] = last_pairs[last_pair] + 1
            print("Seen this last pair before")
             
        # Counting single letter occurrences 
        for l in word: 
            print("letter") # Loop through each letter
            if l not in letters: # If it is a new letter set it to 1
                letters[l] = 1
                print("First time seeing this letter")
            else : # If we have seen it before, add another 1 to the previous count
                letters[l] = letters[l] + 1
                print("I have seen this letter before")

# Loop to find the most common letter
for ltr in letters :
    if letters[ltr] > count:
        count = letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
        
# Probability of each letter occurring
vals = letters.values()
total = sum(vals)
p = n+1

print('Most Common Letter')
prob_dict = {}
for k, v in letters.items():
    prob_dict[k] = (v / total)*100
    print("probabililty of", k, "=", prob_dict[k], "%")
    
print("Probability of Starting Pairs")
first_pair_prob = {}
for k,v in first_pairs.items():
    first_pair_prob[k] = (v/p)*100
    print("probabililty of", k, "=", first_pair_prob[k], "%")
    
print("Probability of Ending Pairs")
last_pair_prob = {}
for k,v in last_pairs.items():
    last_pair_prob[k] = (v/p)*100
    print("probabililty of", k, "=", last_pair_prob[k], "%")
    
# Most common first letter
print('Most Common First Letter')
first_dict = {}
for k, v in first_letters.items():
    first_dict[k] = (v / p)*100
    print("probabililty of", k, "=", first_dict[k], "%")
count = 0
for ltr in first_letters :
    if first_letters[ltr] > count:
        count = first_letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
# Most common starting letter is 'S'
plt.bar(list(first_letters.keys()), first_letters.values(), color='b')
plt.title("Most Common First Letter")
plt.show()

# Most common second letter
print('Most Common Second Letter')
second_dict = {}
for k, v in second_letters.items():
    second_dict[k] = (v / p)*100
    print("probabililty of", k, "=", second_dict[k], "%")
count = 0
for ltr in second_letters :
    if second_letters[ltr] > count:
        count = second_letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
# Most common second letter is 'A'
plt.bar(list(second_letters.keys()), second_letters.values(), color='b')
plt.title("Most Common Second Letter")
plt.show()
        
# Most common third letter
print('Most Common Third Letter')
third_dict = {}
for k, v in third_letters.items():
    third_dict[k] = (v / p)*100
    print("probabililty of", k, "=", third_dict[k], "%")
count = 0
for ltr in third_letters :
    if third_letters[ltr] > count:
        count = third_letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
# Most common third letter is 'A'
plt.bar(list(third_letters.keys()), third_letters.values(), color='b')
plt.title("Most Common Third Letter")
plt.show()

# Most common fourth letter
print('Most Common Fourth Letter')
fourth_dict = {}
for k, v in fourth_letters.items():
    fourth_dict[k] = (v / p)*100
    print("probabililty of", k, "=", fourth_dict[k], "%")
count = 0
for ltr in fourth_letters :
    if fourth_letters[ltr] > count:
        count = fourth_letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
# Most common fourth letter is 'E'
plt.bar(list(fourth_letters.keys()), fourth_letters.values(), color='b')
plt.title("Most Common Fourth Letter")
plt.show()

# Most common fifth letter
print('Most Common Fifth Letter')
fifth_dict = {}
for k, v in fifth_letters.items():
    fifth_dict[k] = (v / p)*100
    print("probabililty of", k, "=", fifth_dict[k], "%")
count = 0
for ltr in fifth_letters :
    if fifth_letters[ltr] > count:
        count = fifth_letters[ltr]
        max_letter = ltr
print("The letter that appears most is:", max_letter,"with", count, "occurrences")
# Most common fifth letter is 'E'
plt.bar(list(fifth_letters.keys()), fifth_letters.values(), color='b')
plt.title("Most Common Fifth Letter")
plt.show()

#import pprint
#pprint.pprint(sorted(prob_dict.items()))
#pprint.pprint(sorted(first_pair_prob.items()))
#print(sorted(prob_dict.items()))

# Plotting the histogram
plt.bar(list(letters.keys()), letters.values(), color='g')
plt.title("Occurrences of Letters")
plt.show()


