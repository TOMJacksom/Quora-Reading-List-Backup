from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from time import sleep
from file_io import *

# SO FAR THIS WORKS FOR ANSWERS ONLY (I WILL ADD SAVED QUESTIONS IN THE FUTURE)
# SO FAR THIS WORKS FOR CHROME ONLY, (I WILL ADD MOZILLA IN THE FUTURE)
# SO FAR THIS WORKS FOR CLASSIC LOGIN AND AUTO-GOOGLE LOGIN (WILL ADD FACEBOOK LOGIN IN THE FUTURE)
# IF IT'S NOT WORKING CORRECTLY IT MEANS THAT QUORA CHANGED IT'S HTML CODE
# THIS IS TOTALLY DEPENDANT ON THE HTML CODE OF QUORA SO IT NEEDS TO BE UPDATED CONSTANTLY


# IF YOU ARE NOT LOGGED IN TO QUORA - UNCOMMENT THE CODE BELLOW (start-end)
# start
# browser = webdriver.Chrome(executable_path="C:\Python27\chromedriver.exe")
# browser.get('https://www.quora.com/reading_list/all')
# browser.maximize_window()
# quoraElems = browser.find_elements_by_xpath("//form/div/div/input")
# emailQuora = quoraElems[0]
# passwordQuora = quoraElems[1]
# emailQuora.send_keys("yourEmail@email.com")  # Your email address
# passwordQuora.send_keys("yourpassword")  # Your password
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
# if you have many/few answers change the number at while (12) to a bigger/smaller number(I have 160 so 12 is ok for me)
browser.get('https://www.quora.com/reading_list/all')
i = 0
while i < 0:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    i += 1

# Identifies answers by the '(more)' element
answers = browser.find_elements_by_link_text('(more)')

j = 1
print('The number of answers: ' + str(len(answers)) + '\n')
for answer in answers:
    if j < len(answers):
        if j == 1:
            browser.execute_script("window.scrollTo(0, 0);")
            ActionChains(browser).click(answers[0]).perform()
            j += 1
        elif j < len(answers) - 1:
            ActionChains(browser).move_to_element(answers[j]).click(answer).perform()
            j += 1
            if j == len(answers) - 1:
                ActionChains(browser).move_to_element(answers[j]).click(answers[j-1]).perform()
                continue
    if j == len(answers) - 1:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(browser).click(answers[j]).perform()
        break
    sleep(2)

# after the scrolling and the clicking is done, the scraping can begin :)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')


# This section of the code creates the directory and the reading_list text file which has all the content in it
dir_name = 'Quora Reading List'

create_project_dir(dir_name)

create_data_file(dir_name, '')

for list_item in soup.find_all('div', {'class': 'pagedlist_item'}):
    # Gets the question title
    question_title = list_item.find('span', {'class': 'question_text'})
    title = question_title.text
    print title + '\n'
    # Iterates through elements and checks each one so it can perform suitable actions
    answer_content = list_item.find('div', {'class': 'ExpandedQText ExpandedAnswer'})
    span_qtext = answer_content.find('span', {'class': 'rendered_qtext'})
    just_text = True
    for element in span_qtext:
        if element.name == 'p':
            just_text = False
            elem = element.attrs
            if 'qtext_para' in elem['class']:
                print element.text + '\n'
        elif element.name == 'ol':
            just_text = False
            ol_elements = element.find_all('li')
            counter = 1
            for li in ol_elements:
                print str(counter) + li.text + '\n'
                counter += 1
        elif element.name == 'ul':
            just_text = False
            ul_elements = element.find_all('li')
            for li in ul_elements:
                print li.text + '\n'
        elif element.name == 'br':
            print '<br>' + '\n'
        elif element.name == 'None':
            print element.text + '\n'
        else:
            continue
    # writing = content.encode('utf-8')
    # append_to_file('Quora Reading List' + '/reading_list.txt', writing)





