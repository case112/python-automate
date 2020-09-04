import bs4
import requests
import os
import shutil
import sys

#print('Album first image link here:')
url = 'http://fotoalbum.ee/photos/Meriliiin/101783435'
token = True
img_no = 0

#get file name
try:
    res = requests.get(url)
    res.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
album_name_soup = soup.select('.breadcrumbs > a:nth-child(2)')

if album_name_soup == []:
    sys.exit("This is not a valid URL. Try again.")

album_name = album_name_soup[0].text.strip().lower().replace(".", "").replace(",", "").replace(" ", "") 
print('Downloading from album: ' + album_name)

if not os.path.exists(os.getcwd() + album_name):
    os.makedirs(album_name, exist_ok=True)

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

        img_path = os.getcwd() + os.path.sep + album_name + os.path.sep + album_name + '_img_' + img_no + '.jpg'
        image_name = album_name + '_img_' + img_no + '.jpg'
        print("Get - " + image_name)

        with open(img_path, 'wb') as f:
            img_request.raw.decode_content = True
            shutil.copyfileobj(img_request.raw, f) 


    next_element = soup.select('.next')
    if next_element == []:
        print('Reached to the end of the album, downloaded ' + img_no + 'images.')
        token = False
    else:
        for link in next_element:
            next_url = link.get('href')
            next_url = 'http://fotoalbum.ee' + next_url
            #print(next_url)
            url = next_url

