#!/usr/bin/env python3.7

import bs4
import requests
import os
import shutil
import sys
import random
import re

print('')
print('####################################################')
print('----------------------------------------------------')
print('Fotoalbumi piltide allalaadimist lihtsustav rakendus')
print('----------------------------------------------------')
print('')
print('Kleebi siia pildi URL, rakendus proovib alla laadida ')
print('selle ja kõik sellele järgnevad pildid valitud')
print('albumis ')
print('(kujul: http://fotoalbum.ee/photos/kasutaja/83997/)')
print('')

url = input(':  ') 
print('----------------------------------------------------')
print('')
token = True
img_no = 0
random_number = random.randint(1,99)
random_number = '_' + str(random_number)

try:
    res = requests.get(url)
    res.raise_for_status()
except requests.exceptions.HTTPError:
    print('')
    input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")
except requests.exceptions.MissingSchema: 
    print('')
    input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")
except requests.exceptions.ConnectionError:
    print('')
    input('Interneti ühendus puudub, proovi uuesti  ')
    sys.exit("")
except requests.exceptions.InvalidURL:
    print('')
    input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")


soup = bs4.BeautifulSoup(res.text, 'html.parser')
album_name_soup = soup.select('.breadcrumbs > a:nth-child(2)')
try:
    images_to_download_soup = soup.find(class_='breadcrumbs').find_all(text=True, recursive=False)
except AttributeError:
    print('')
    input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")

if album_name_soup == []:
    print('')
    input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")

album_name_long = album_name_soup[0].text.strip()
album_name = album_name_soup[0].text.strip().lower()
album_name = re.sub('[\W_]+', '', album_name)
images_to_download = str(images_to_download_soup)
images_to_download = images_to_download[images_to_download.find("(")+1:images_to_download.find(")")].split('/')
current_image = int(images_to_download[0])
total_images = int(images_to_download[1])
images_to_download = total_images - current_image + 1 
print('Leidsin ' + str(images_to_download) + ' pilti albumist - ' + str(album_name_long))
print('')
answer = input('Kas jätkan allalaadimist? (jah/ei): ')
print('----------------------------------------------------')
print('')

if answer.lower() != 'jah':
    input('Soovisid töö katkestada, vajuta enter klahvile et programm sulgeda ')
    sys.exit("")

if not os.path.exists(os.path.expanduser("~/Desktop") + os.path.sep + album_name + random_number):
    os.makedirs(os.path.expanduser("~/Desktop") + os.path.sep + album_name + random_number, exist_ok=True)

while token == True:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_element = soup.select('.photo-full > span:nth-child(1) > img:nth-child(1)')


    for link in image_element:
        image_url = link.get('src')[2:]
        image_url = 'http://' + image_url
        #print(image_url)


    img_request = requests.get(image_url, stream=True)
    if img_request.status_code == 200:
        img_no = int(img_no)
        img_no += 1
        img_no = str(img_no)

        img_path = os.path.expanduser("~/Desktop") + os.path.sep + album_name + random_number + os.path.sep + 'img_' + img_no + '_' + album_name + '.jpg'
    
        image_name = 'img_' + img_no + '_' + album_name + '.jpg'
        print("Tõmban pilti - " + image_name)

        with open(img_path, 'wb') as f:
            img_request.raw.decode_content = True
            shutil.copyfileobj(img_request.raw, f) 


    next_element = soup.select('.next')
    if next_element == []:
        print('----------------------------------------------------')
        print('')
        print('Jõudsin albumi lõppu, laadisin alla ' + img_no + ' pilti')
        print('----------------------------------------------------')
        print('')
        token = False
    else:
        for link in next_element:
            next_url = link.get('href')
            next_url = 'http://fotoalbum.ee' + next_url
            #print(next_url)
            url = next_url



print('Paigutasin pildid sinu töölauale ' + str(album_name) + random_number + ' kausta')
print('----------------------------------------------------')
print('')
input('Väljumiseks vajuta enter klahvi ' )
print('')