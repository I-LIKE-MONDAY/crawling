# ch06/ex3.py : chromedriver.exe를 지정한 위치에 저장

from selenium import webdriver

wd = webdriver.Chrome('./WebDriver/chromedriver.exe')

wd.get('https://www.hanbit.co.kr/')