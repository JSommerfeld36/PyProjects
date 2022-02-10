#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:44:16 2022

@author: joelsommerfeld
"""

# MAD LIBS

noun = input("Pick a noun: ")
verb = input("Pick a verb: ")
name = input("Pick a name: ")
adjective = input("Pick an adjective: " )
noun2 = input("Pick a noun: ")
place = input("Name a place: ")
colour = input("Pick a colour: ")
emotion = input("Pick an emotion: ")

# Write something elegant to make all the words lower case except for the name and place
word_list = [x.lower() for x in [noun, verb, adjective, noun2, colour, emotion]]
caps = [y.capitalize() for y in [name, place]]

print("The giant", word_list[4], word_list[0], "was all that stood between", caps[0], "and the", word_list[3], "but all", caps[0], "wanted to do was to go home to", caps[1],"and", word_list[1],". Is that so much to ask?!, they cried out aloud in", word_list[5],". What a", word_list[2], "week.")

