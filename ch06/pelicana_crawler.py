# ch06/pelicana_crawler.py : 페리카나 매장 정보 크롤링

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd

def pelicana_store(result):
  for page in range(1, 108):
    pelicana_url = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' % page
    # print(pelicana_url)
    html = urllib.request.urlopen(pelicana_url)
    soupPelicana = bs(html, 'html.parser')
    tag_body = soupPelicana.find('tbody')
    # print(tag_body)

    for store in tag_body.find_all('tr'):
      store_td = store.find_all_next('td')
      # print(store_td)
      store_name = store_td[0].string
      store_address = store_td[1].string
      store_phone = store_td[2].string
      print('%s %s %s' % (store_name, store_address, store_phone))
      result.append([store_name] + [store_address] + [store_phone])


def main():
  result = []
  pelicana_store(result)
  pelicana_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
  pelicana_tbl.to_csv('./data/pelicana.csv', encoding='cp949', mode='w', index=True)
  print('------ 완료 ------')
  del result[:]

if __name__ == '__main__':
  main()
