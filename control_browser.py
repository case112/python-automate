from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.okidoki.ee/')

search_element = browser.find_element_by_css('.query > input:nth-child(1)')

search_element.send_keys('4k uhd')

search_element.submit()