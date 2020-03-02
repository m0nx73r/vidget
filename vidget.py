import mechanize
import re
import sys
import requests
import config
from random import randint
from bs4 import BeautifulSoup
from urllib.parse import unquote
br = mechanize.Browser()
br._factory.is_html = True
br.set_handle_robots(False)
br.set_handle_refresh(False)
randnum = randint(10000000, 99999999)
br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
#Open URL and submit
br.open("https://www.facebook.com/login.php") #login page
user = (config.user) #your username
passwd = (config.passwd) #your password
br.select_form(nr=0)
br["email"] = user
br["pass"] = passwd
br.submit() #Submit
print('Logged in successfully! \n')

vid_link = input("Enter video URL : ")
vid_link_stripped = vid_link.lstrip('https://www.')
vid_link_fresh = "https://mbasic." + str(vid_link_stripped)
r = requests.get(str(vid_link_fresh))
br.open(vid_link_fresh)
soup = BeautifulSoup(br.response().read(), 'html.parser')


print("DOOWNLOADING VIDEO!" + '\n')
data = soup.find_all('a', href=True)
for link in soup.findAll('a', href=re.compile('video')):
    links = link.get('href')
    stripped_link = links.strip('/video_redirect/?src=')
    unquotted_link = unquote(stripped_link)
    vid = requests.get(unquotted_link, stream=True)
    with open(str(randnum) + ".mp4", 'wb') as f:
        f.write(vid.content)
        print('VIDEO DOWNLOADED!!!')
