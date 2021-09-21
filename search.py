# coding: UTF-8
import pandas as pd
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')

dt_now = datetime.datetime.now()

# launch browser
browser = webdriver.Chrome(options=options)

saunas = list()

# scraping
for i in range(1, 5):
    url = f'https://sauna-ikitai.com/saunas/{i}'
    try:
        browser.get(url)
        sauna = {
            'name': browser.find_element_by_class_name('c-headline_string').text,
            'place': browser.find_element_by_class_name('p-saunaDetailHeader_area').text,
            'room_temp': browser.find_element_by_xpath(
                f'//div[@class=\'p-saunaSpecItem p-saunaSpecItem--sauna\']/p').text[3:],
            'mizuburo_temp': browser.find_element_by_xpath(
                f'//div[@class=\'p-saunaSpecItem p-saunaSpecItem--mizuburo\']/p').text[3:],
            'activities': browser.find_element_by_class_name('p-localNav_count').text
        }
        saunas.append(sauna)
        print(browser.find_element_by_class_name('c-headline_string').text)
    except Exception as NoSuchElementException:
        pass

browser.close()

names = list()
place = list()
room_temp = list()
mizuburo_temp = list()
activities = list()

for sauna in saunas:
    names.append(sauna['name'])
    place.append(sauna['place'])
    room_temp.append(sauna['room_temp'])
    mizuburo_temp.append(sauna['mizuburo_temp'])
    activities.append(sauna['activities'])

now = dt_now.strftime('%Y%m%d_%H%M%S')

# CSV output
df = pd.DataFrame()

df['施設名'] = names
df['場所'] = place
df['サ活'] = activities
df['サウナ室'] = room_temp
df['水風呂'] = mizuburo_temp

df.to_csv(f'./data/サウナ情報_{now}.csv')
