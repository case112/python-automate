import bs4
import requests
import os
import shutil
import sys
import re


base_url = 'base_url'
initial_url = 'initial_url'
token = True

print('')
print('####################################################')
print('')

#start session
try:
    with requests.Session() as session:
        cookie = {'PHPSESSID': 'beb954415ec509d84ff70ad3e2ded9de'}
        response = session.post(initial_url, cookies=cookie)
        #print(response)
        #print(session)
except:
    print('Cant establish session')
    sys.exit("")

def get_page(url):
    try:
        res = session.get(url, cookies=cookie)
        res.raise_for_status()
        #print(res)
        print('GET: ' + url)
        return res
    except requests.exceptions.HTTPError:
        print('')
        input('HTTPERROR')
        sys.exit("")
    except requests.exceptions.MissingSchema: 
        print('')
        input('MISSINGSCEMA')
        sys.exit("")
    except requests.exceptions.ConnectionError:
        print('')
        input('Interneti ühendus puudub, proovi uuesti  ')
        sys.exit("")
    except requests.exceptions.InvalidURL:
        print('')
        input('Vigane URL, proovi uuesti, vajuta enter klahvile et programm sulgeda ')
        sys.exit("")


soup = bs4.BeautifulSoup(get_page(initial_url).text, 'html.parser')

partial_edit_link = soup.select('.main > li')[1].find("a").attrs['href']

#print(partial_edit_link)
edit_link = base_url + partial_edit_link

#print(edit_link)

soup = bs4.BeautifulSoup(get_page(edit_link).text, 'html.parser')
input_block = soup.find_all(attrs={"name" : "links[]"})
#soup = bs4.BeautifulSoup(get_page(edit_link).text, 'html.parser')
form_block = soup.find_all(attrs={"class" : "frm"})[-1]
form_action =  base_url + form_block['action']

print(input_block)
print(form_action)
input_values = []

for item in input_block:
    value = item['value'].strip()
    if 'http://' in value:
        print('change http to https')
        value = value[:4] + 's' + value[4:]
        input_values.append(value)
        item['value'] = value
    else:
        print('https, no action')
        input_values.append(value)
    
print(input_block)

payload = {
    
    }

payload['title'] =  soup.find("input", {"name":"title"})['value']
payload['county'] =  soup.find("option", {"selected":"selected"})['label']
#payload['parish'] =  soup.find_all("option", {"selected":"selected"})['label']
payload['address'] =  soup.find("input", {"name":"address"})['value']


# tuleks seda proovida, kas siis teeb p'riselt posti
# kui ja ssiis kui teeb tuleb saata need uued valued kaasa parameetritena
#response2 = session.post(form_action, cookies=cookie)


print(payload)

