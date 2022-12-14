# ch06/pelicana_crawler.py : 페리카나 매장 정보 크롤링

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime, time
from itertools import count

import ssl  # 접속보안 허용


def get_request_url(url, enc='utf-8'):
  req = urllib.request.Request(url)
  try:
    # [SSL: CERTIFICATE_VERIFY_FAILED] 에러 뜰때
    ssl._create_default_https_context = ssl._create_unverified_context  # 접속보안 허용
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
      try:
        rcv = response.read()
        # 한글로 변환
        ret = rcv.decode(enc)
      except UnicodeDecodeError:
        # replace : 에러 발생시 ?로 변환이 된다
        ret = rcv.decode(enc, 'replace')
      return ret
  except Exception as e:
    print(e)
    print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
    return None


def getPelicanaAddress(result):
  for page_idx in count():
    # print(page_idx)
    # time.sleep(1)
    url = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' % str(page_idx + 1)
    # print('[Pelicana Page] : [%s]' % str(page_idx + 1))

    rcv_data = get_request_url(url)
    soupData = BeautifulSoup(rcv_data, 'html.parser')
    store_table = soupData.find('table', attrs={'class': 'table mt20'})
    tbody = store_table.find('tbody')
    # print(tbody)
    bEnd = True
    for store_tr in tbody.findAll('tr'):
      bEnd = False
      tr_tag = list(store_tr.strings)
      store_name = tr_tag[1]
      store_address = tr_tag[3]
      store_sido_gu = store_address.split()[:2]
      result.append([store_name] + store_sido_gu + [store_address])
    if(bEnd == True): # 확인용 코드
      print(result[0])
      print('== 데이터 수 : %d ' % len(result))
      return
  return



def cswin_pelicana():
  result = []
  print('Pelicana Address Crawling Start')
  getPelicanaAddress(result)
  pelicana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
  pelicana_table.to_csv('./data/pelicana4.csv', encoding='cp949', mode='w', index=True)
  del result[:]
  print('------------- 끝 -------------')


if __name__ == '__main__':
  cswin_pelicana()
