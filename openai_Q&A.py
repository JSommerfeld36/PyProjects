#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 17:58:40 2023

@author: joelsommerfeld
"""

import openai
openai.organization = "org-ImcRGGR1v3duTpgJvewZZirM"
api_key=open("/Users/joelsommerfeld/Desktop/api_key.txt", "r").read()
openai.api_key = api_key.strip()
openai.Model.list()

# Now let's use the API
prompt = input("Type a question: ")

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message.strip())
