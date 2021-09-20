# coding: UTF-8
from selenium import webdriver
from dotenv import load_dotenv
import os

# load envfile
load_dotenv()
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
URL = os.getenv('URL')


# launch browser
browser = webdriver.Chrome()
browser.get(URL)


# GET Elements
elm_username = browser.find_element_by_name('username')
elm_password = browser.find_element_by_name('password')
elm_login_btn = browser.find_element_by_class_name('login-button')


# LOGIN
elm_username.send_keys(USER_NAME)
elm_password.send_keys(PASSWORD)
elm_login_btn.click()
