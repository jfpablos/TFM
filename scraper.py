# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:11:19 2019

@author: 46856585
"""
import boto3
import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

url = {
    'google': 'https://www.google.com/search?q=ibex+35&lr=&cr=countryES&hl=es&tbs=ctr:countryES&source=lnms&tbm=nws',
    'bing': 'https://www.bing.com/news/search?q=ibex+35&cc=es',
    'yahoo': 'https://es.news.search.yahoo.com/search?p=ibex+35',
    'duck': 'https://duckduckgo.com/?q=ibex+35&t=h_&iar=news&ia=news&kl=es-es&df=d',
    'qwant' : 'https://www.qwant.com/?q=ibex+35&t=news&r=ES',
    'ibex': 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'
    }

def lambda_handler(event, context):
    
    with open('prueba.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([datetime.now(), google(), bing(), yahoo(), duck(), qwant()])

    pass

def google():
  try:
    page = requests.get(url['google']).text
  except:
    print('hay problemas')  
  soup = BeautifulSoup(page, "html.parser")
  text = [t.find('h3').text + '. ' + t.find(class_="st").text for t in soup.find_all("div", {"class" :"g"})]
  text = ' '.join(text)
  return text

def bing():
  page = requests.get(url['bing']).text
  soup = BeautifulSoup(page, "html.parser")
  text = [t.find(class_='title').text + '. ' + t.find(class_='snippet').text for t in soup.find_all('div', class_='t_s')]
  text = ' '.join(text)
  return text

def yahoo():
  page = requests.get(url['yahoo']).text
  soup = BeautifulSoup(page, "html.parser")
  text = [p.find('h3').text + '. ' + p.find('p').text for p in soup.find(class_='searchCenterMiddle').find_all('li')]
  text = ' '.join(text)
    
  return text

def duck():
  wd.get(url['duck'])
  text = [t.text for t in wd.find_elements_by_xpath("//div[@class='results js-vertical-results']/div/div/h2/a")]
  text = list(filter(None, text))
  text = '. '.join(text)
  return text

def qwant():
  wd.get(url['qwant'])
  text = [t.text for t in wd.find_elements_by_xpath("//div[@class='result-type__news__item']/div[@class='result-type__news__text--container']/a")]
  text = ' '.join(text)
  return text