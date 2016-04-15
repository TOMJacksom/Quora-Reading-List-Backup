from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from time import sleep
#Quora Login

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data')

browser = webdriver.Chrome(executable_path="C:\Python27\chromedriver.exe", chrome_options=options)

browser.get('https://www.quora.com/reading_list/all')
i = 0
while i < 2:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    i += 1

#html = browser.page_source
#soup = BeautifulSoup(html)
#print soup.prettify('utf-8')

answers = browser.find_elements_by_link_text('(more)')
print answers
for answer in answers:
    ActionChains(browser).move_to_element(answer).click(answer).perform()
    sleep(1)

#quoraElems = browser.find_elements_by_xpath("//form/div/div/input")
#emailQuora = quoraElems[0]
#passwordQuora = quoraElems[1]
#emailQuora.send_keys("#Email")
#passwordQuora.send_keys("#Password")
#passwordQuora.send_keys(Keys.RETURN)
