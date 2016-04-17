from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from time import sleep

# SO FAR THIS WORKS FOR ANSWERS ONLY (I WILL ADD SAVED QUESTIONS IN THE FUTURE)
# SO FAR THIS WORKS FOR CHROME ONLY, (I WILL ADD MOZILLA IN THE FUTURE)
# SO FAR THIS WORKS FOR CLASSIC LOGIN AND AUTO-GOOGLE LOGIN (WILL ADD FACEBOOK LOGIN IN THE FUTURE)
# IF IT'S NOT WORKING CORRECTLY IT MEANS THAT QUORA CHANGED IT'S HTML CODE
# THIS IS TOTALLY DEPENDANT ON THE HTML CODE OF QUORA SO IT NEEDS TO BE UPDATED CONSTANTLY


# IF YOU ARE NOT LOGGED IN TO QUORA - UNCOMMENT THE CODE BELLOW (start-end)
# start
# browser = webdriver.Chrome()
# browser.get('https://www.quora.com')
# quoraElems = browser.find_elements_by_xpath("//form/div/div/input")
# emailQuora = quoraElems[0]
# passwordQuora = quoraElems[1]
# emailQuora.send_keys("your_email@email.com")  # Your email address
# passwordQuora.send_keys("yourpassword123")  # Your password
# passwordQuora.send_keys(Keys.RETURN)
# end

# IF YOU ARE LOGGED IN TO QUORA WITH GOOGLE AND LOGGED ON TO CHROME AUTOMATICALLY AFTER STARTUP
# OTHERWISE COMMENT OUT THE CODE BELLOW
# start
options = webdriver.ChromeOptions()
# PROVIDE YOUR OWN PATH TO YOUR USER DATA
options.add_argument('user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data')
# PROVIDE YOUR OWN PATH TO THE CHROME WEB-DRIVER EXECUTABLE (DOWNLOAD IT IF YOU DON'T HAVE IT)
browser = webdriver.Chrome(executable_path="C:\Python27\chromedriver.exe", chrome_options=options)
# end

# this part goes to the Quora Reading List page (all answers), and scrolls all the way to the bottom (that will
# take some time, depending on how many answers you have saved)
# after that it will start to click "(more)" for each answer
# sleep(5) means wait 5 seconds before the next scroll down so everything can load
# if your internet is not as crappy as mine you can change it to less so the scrolling and clicking can take less time
browser.get('https://www.quora.com/reading_list/all')
i = 0
while i < 12:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    i += 1

answers = browser.find_elements_by_link_text('(more)')
# helper = browser.find_elements_by_class_name('CredibilityFact')

j = 1
print('The number of answers: ' + str(len(answers)) + '\n')
for answer in answers:
    if j < len(answers):
        if j == 1:
            browser.execute_script("window.scrollTo(0, 0);")
            ActionChains(browser).click(answers[0]).perform()
            j += 1
            print('j in first is: ' + str(j) + '\n')
        elif j < len(answers) - 1:
            ActionChains(browser).move_to_element(answers[j]).click(answer).perform()
            j += 1
            print('j in normal is: ' + str(j) + '\n')
            if j == len(answers) - 1:
                ActionChains(browser).move_to_element(answers[j]).click(answers[j-1]).perform()
                continue
    if j == len(answers) - 1:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(browser).click(answers[j]).perform()
        print('j in last is: ' + str(j) + '\n')
        break
    sleep(2)

# after the scrolling and the clicking is done, the scraping can begin :)
html = browser.page_source
soup = BeautifulSoup(html)
# print soup.prettify('utf-8')
