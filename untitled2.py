#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:30:50 2020

@author: kali
"""

from newsapi import NewsApiClient
import requests
from selenium import webdriver
from datetime import datetime,timedelta
from datetime import date
today = date.today()


now = datetime.now()


current= now.strftime("%H:%M:%S")
d = now - timedelta(hours=0, minutes=30)
curr2=d.strftime("%H:%M:%S")
times=str(today)+'T'+current
times2=str(today)+'T'+curr2
#keywords = ["hollywood", "movies"]
   
#url = ('https://newsapi.org/v2/top-headlines?q=' + ' OR '.join(keywords)) + '&language=en' +'&from=(today)'+'&to=(times)' + '&apiKey=8e268e93d817478598e019b0351c567a' 
url = 'https://newsapi.org/v2/everything?'
secret='8e268e93d817478598e019b0351c567a'
# Specify the query and number of returns
parameters = {
    'q': 'soya', # query phrase
    'from': times,
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}


   
open_page = requests.get(url,params=parameters).json() 
article = open_page["articles"] 
  


results = [] 
  
for ar in article: 
    results.append(ar["url"])