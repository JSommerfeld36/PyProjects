#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:06:46 2023

@author: joelsommerfeld
"""

# pip install requests
# pip install beautifulsoup4
# pip install schedule

import requests
from bs4 import BeautifulSoup
import schedule
import time

def get_amazon_price(url):
    print("Fetching price....")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        print(response.content)


        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find(id='priceblock_ourprice')
        print("here")
        if not price_element:
            price_element = soup.find(id='priceblock_dealprice')

        if price_element:
            price = price_element.get_text()
            return price.strip()
        else:
            return None

    except Exception as e:
        print(f"Error occurred while fetching price: {e}")
        return None

def track_price(url):
    product_price = get_amazon_price(url)
    if product_price:
        print(f"Current price: {product_price}")
        # Here, you can add your code to compare and track price changes as per your requirements.

def main():
    # Replace this URL with the product you want to track.
    amazon_url = "https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0BDHWDR12/ref=sr_1_1_sspa?crid=2W36LH8PY5ZQV&keywords=airpods+pro&qid=1691197800&s=electronics&sprefix=airpods%2Celectronics%2C122&sr=1-1-spons&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    track_price(amazon_url)

# Uncomment the following line if you want the script to run every hour.
# schedule.every().hour.do(main)

# Uncomment the following line if you want the script to run every day at a specific time.
# schedule.every().day.at("10:00").do(main)

# Uncomment the following line if you want the script to run every weekday at a specific time.
# schedule.every().monday.at("10:00").do(main)
# schedule.every().tuesday.at("10:00").do(main)
# schedule.every().wednesday.at("10:00").do(main)
# schedule.every().thursday.at("10:00").do(main)
# schedule.every().friday.at("10:00").do(main)

# Uncomment the following line if you want the script to run every minute (for testing purposes).
# schedule.every(1).minutes.do(main)

# The script will run until you manually stop it.
while True:
    schedule.run_pending()
    time.sleep(1)
