import bs4
import requests
import os
import shutil
import sys

#print('Album first image link here:')
url = 'http://fotoalbum.ee/photos/Meriliiin/99677478'
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
images_to_download_soup = soup.find(class_='breadcrumbs').find_all(text=True, recursive=False)

if album_name_soup == []:
    sys.exit("This is not a valid URL. Try again.")

album_name = album_name_soup[0].text.strip().lower().replace(".", "").replace(",", "").replace(" ", "")
images_to_download = str(images_to_download_soup)
images_to_download = images_to_download[images_to_download.find("(")+1:images_to_download.find(")")].split('/')
current_image = int(images_to_download[0])
total_images = int(images_to_download[1])
images_to_download = total_images - current_image + 1 
print('You are about to download ' + str(images_to_download) + ' images from album: ' + album_name)
input('Continue? (y/n)')

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

        img_path = os.getcwd() + os.path.sep + album_name + os.path.sep + 'img_' + img_no + '_' + album_name + '.jpg'
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

