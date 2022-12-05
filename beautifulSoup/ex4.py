# ex4.py

import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://news.daum.net/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

# item_issue = soup.find_all('div', {'class': 'item_issue'})

# for issue in item_issue:
  # print(issue.text)

# print(soup.find_all('a')[:5]) # a태그 [5]까지

# for i in soup.find_all('a')[0:10]:
#   print(i.get('href'))  # a태그의 0~10 index 가져오고 그 내부 href 속성 값 가져오기

# for i in soup.find_all('div', class_='item_issue'):
#   print(i.find_all_next('a'))

for i in soup.find_all('div', {'class': 'item_issue'}):
  # ah = i.find_all('a')[0].get('href')
  # print(ah)
  soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
  print(soup2)
