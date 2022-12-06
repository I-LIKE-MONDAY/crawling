# pip install beautifulSoup
# beautifulSoup/nvCrawler.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.naver.com')
obj = BeautifulSoup(html, 'html.parser')

for meta in obj.head.find_all('meta'):  # 전체 html 태그에서 head 태그의 meta 태그 찾기
  print(meta.get('content'))  # meta 태그 내의 content 내용을 출력

print('----------------------------------------------------------------------------------')
print(obj.head.find('meta', {'name':'description'}).get('content')) # meta태그 내의 name이 description인 태그의 content를 출력

print('----------------------------------------------------------------------------------')
for link in obj.find_all('a'):  # a 태그를 다 찾아라
  print(link.text.strip(), link.get('href'))