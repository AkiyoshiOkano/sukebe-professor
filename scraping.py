# coding: UTF-8
import requests
import urllib2
import chardet
import cv2
from bs4 import BeautifulSoup
import codecs
import io
import pickle
import os

# アクセスするURL
url = "https://www.caribbeancom.com/actor/"

# URLにアクセスする htmlが帰ってくる
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

div_tags = soup.find_all("div", attrs={"class": "actor-list-area"})

av_actor_name_list = []
for div_tag in div_tags:
	li_tags = div_tag.find_all("li")

	for li_tag in li_tags:
	  image_url = "https://www.caribbeancom.com" + li_tag.find("img")['src']
	  actor_name = li_tag.find("span").string
	  av_actor_name_list.append(actor_name)
	  print(actor_name)

	  print("Downloading " + actor_name)
	  req = requests.get(image_url)
	  if req.status_code == 200:
	  	os.makedirs(actor_name)
	  	f = open(actor_name + "/" + actor_name + ".jpg", 'wb')
	  	f.write(req.content)
	  	f.close()
