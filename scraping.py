# coding: UTF-8
import requests
import urllib2
import chardet
import cv2
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.caribbeancom.com/actor/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

div_tags = soup.find_all("div", attrs={"class": "actor-list-area"})

index = 0
av_actor_list = []
for div_tag in div_tags:
	print("----------------------------------------")
	li_tags = div_tag.find_all("li")

	for li_tag in li_tags:
	  image_url = "https://www.caribbeancom.com" + li_tag.find("img")['src']
	  actor_name = li_tag.find("span").string

	  print "Downloading " + actor_name
	  req = requests.get(image_url)
	  if req.status_code == 200:
	  	f = open(actor_name + ".jpg", 'wb')
	  	f.write(req.content)
    	f.close()
    	print "complete!"

