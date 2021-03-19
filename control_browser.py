from selenium import webdriver

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

browser = webdriver.Firefox(firefox_profile=firefox_profile, executable_path = '/usr/local/bin/geckodriver')


browser.get('https://www.okidoki.ee/')

search_element = browser.find_element_by_css('.query > input:nth-child(1)')

search_element.send_keys('4k uhd')

search_element.submit()