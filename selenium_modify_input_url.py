from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


base_url = 'https://testkeskkond.ee'
edit_url =  base_url + 'admin.php?menuID=archivalmaterial&action=view&edit=1&id='
username = 'user'
password = 'pw'
search_string = 'http://testkeskkond'

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get(base_url)

def login():
    login_form = browser.find_element_by_id('button-login')
    login_form.click()
    username_element = browser.find_element_by_name('username')
    username_element.send_keys(username)
    pw_element = browser.find_element_by_name('password')
    pw_element.send_keys(password)
    pw_element.submit()
    time.sleep(3)

def replace_strings(id):
    id = str(id)
    browser.get(edit_url + id)
    element = browser.find_elements_by_xpath("//input[contains(@value, '" + search_string + "')]")
    time.sleep(0.4)
    print(id, end = ', ')

    if element != []:
        for e in element:
            print(e.get_attribute('value'), end = ', ')
            temp_value = e.get_attribute('value').strip()
            e.send_keys(Keys.COMMAND + "a")
            e.send_keys(Keys.DELETE)
            temp_value = temp_value[:4] + 's' + temp_value[4:]
            e.send_keys(temp_value)
            print(temp_value, end = ', ')
            time.sleep(0.2)

        save = browser.find_element_by_xpath("//*[contains(text(), 'Salvesta')]")
        save.click()
        print('saved')
        time.sleep(0.4)

    else:
        print('not saved')

# log in 
login()

# loop through specified archivals
for n in range(1, 7566):
    replace_strings(n)

