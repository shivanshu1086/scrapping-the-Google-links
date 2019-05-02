#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 04:07:50 2019

@author: shivanshu
"""
#Beautiful soup
import bs4
import requests
userInput=input("Enter the searching thing: ")
userInput=userInput.replace(" ","+")
url3="https://www.google.co.in/search?q="+userInput
data3=requests.get(url3)
soup= bs4.BeautifulSoup(data3.text,"lxml")
for links in soup.select(".r a"):
    link=links.get('href')
    res= "https://google.com"+link
    print(res)
    break
#print(soup.prettify())