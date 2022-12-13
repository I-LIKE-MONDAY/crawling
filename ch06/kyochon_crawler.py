# ch06/kyochon_crawler.py : 교촌 영업 매장 크롤링 (정적 웹 크롤링)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime, time
from itertools import count


num = 0
def kyochon_store(result):
    for sido in range(1, 18):
      for gu in range(1, 46):
        try:
          kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido, gu)
          html = urllib.request.urlopen(kyochon_url)
          soupKyochon = BeautifulSoup(html, 'html.parser')
          ul_tag = soupKyochon.find("div", {"class": "shopSchList"})

          for store_data in ul_tag.findAll('a'):
            store_name = store_data.find('strong').get_text()
            store_address = store_data.find('em').get_text().strip().split('\r')[0]
            store_sido_gu = store_address.split()[:2]
            result.append([store_name] + [store_sido_gu] + [store_address])
            print(store_name)
        except:
          pass


def main():
  result = []
  kyochon_store(result)
  kyochon_tbl = pd.DataFrame(result, columns=('store_name', 'store_sido_gu', 'store_address'))
  kyochon_tbl.to_csv('./data/kyochon.csv', encoding='cp949', mode='w', index=True)
  print('------ 완료 ------')
  del result[:]


if __name__ == '__main__':
  main()
