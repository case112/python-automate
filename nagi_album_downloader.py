import bs4
import requests
import os
import shutil

#print('Album first image link here:')
url = 'http://fotoalbum.ee/photos/Meriliiin/98994725/'
token = True
img_no = 0

#get file name
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
file_name = soup.select('.breadcrumbs > a:nth-child(2)')
file_name = file_name[0].text.strip().lower().replace(".", "").replace(",", "").replace(" ", "") 
print(file_name)

while token == True:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_element = soup.select('.photo-full > span:nth-child(1) > img:nth-child(1)')


    for link in image_element:
        image_url = link.get('src')[2:]
        image_url = 'http://' + image_url
        print(image_url)


    img_request = requests.get(image_url, stream=True)
    if img_request.status_code == 200:
        img_no = int(img_no)
        img_no += 1
        img_no = str(img_no)

        if not os.getcwd()(file_name):
            os.makedirs(file_name)
        img_name = os.getcwd() + file_name + '_img_' + img_no + '.jpg'

        with open(img_name, 'wb') as f:
            img_request.raw.decode_content = True
            shutil.copyfileobj(img_request.raw, f) 
 

        #with open(img_name, 'wb') as f:
            #f.write(img_request.content)

    next_element = soup.select('.next')
    if next_element == []:
        print('Reached to the end of the album')
        token = False
    else:
        for link in next_element:
            next_url = link.get('href')
            next_url = 'http://fotoalbum.ee' + next_url
            print(next_url)
            url = next_url

