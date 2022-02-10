#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:00:04 2022

@author: joelsommerfeld
"""

# Guess the Number

import random

num = int(random.randint(1, 10))
attempts = 0
# Guess the number part
w2p = input("Do you want to play a game? It is simple, just guess the number that I am thinking of, nothing to it. Just tell me, yes or no, \n")

while w2p.lower() == "yes":
    guess = input("Pick a number between 1 and 10: ")
    
    if int(guess) == num:
        print("Yay!! You got it!!")
        attempts += 1
        print("That took {} attempts. Nice work!". format(attempts))
        again = input("Do you want to play again? \n")
        attempts = 0
        num = int(random.randint(1, 10))
        if again.lower() == "no":
            print("Fine. I would have won next time anyway.")
            break
    elif int(guess) > num:
        print("Nope, the number I am thinking of is lower")
        attempts += 1
    elif int(guess) < num:
        print("Not quiet. Try a higher number") 
        attempts += 1
        
