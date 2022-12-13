# ch06/kyochon_crawler_2.py : 교촌 영업 매장 크롤링 (정적 웹 크롤링) 해설

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

def getKyochonAddress(sido1, result):
  for sido2 in count():
    url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido1), str(sido2))
    # print(url)
    try:
      rcv_data = get_request_url(url)
      soupData = BeautifulSoup(rcv_data, 'html.parser')
      ul_tag = soupData.find('ul', attrs={'class': 'list'})
      # print(ul_tag)
      for store_data in ul_tag.findAll('a', href=True): # a 태그 내에 href가 있는 a태그만 가져와라
        store_name = store_data.find('strong').get_text()
        # print(store_name)
        store_address = store_data.find('em').get_text().strip().split('\r')[0]
        store_sido_gu = store_address.split()[0:2]
        result.append([store_name] + store_sido_gu + [store_address])
    except:
      break
  return

def cswin_Kyochon():
  result = []
  print('Kyochon Address Crawling Start')
  for sido1 in range(1, 18):
    getKyochonAddress(sido1, result)
  kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
  kyochon_table.to_csv('./data/kyochon3.csv', encoding='cp949', mode = 'w', index=True)
  del result[:]
  print('-------------끝--------------')


if __name__ == '__main__':
  cswin_Kyochon()






# def kyochon_store(result):
#     for sido in range(1, 18):
#       for gu in range(1, 46):
#         try:
#           kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido, gu)
#           html = urllib.request.urlopen(kyochon_url)
#           soupKyochon = BeautifulSoup(html, 'html.parser')
#           ul_tag = soupKyochon.find("div", {"class": "shopSchList"})
#
#           for store_data in ul_tag.findAll('a'):
#             store_name = store_data.find('strong').get_text()
#             store_address = store_data.find('em').get_text().strip().split('\r')[0]
#             store_sido_gu = store_address.split()[:2]
#             result.append([store_name] + [store_sido_gu] + [store_address])
#             print(store_name)
#         except:
#           pass
#
#
# def main():
#   result = []
#   kyochon_store(result)
#   kyochon_tbl = pd.DataFrame(result, columns=('store_name', 'store_sido_gu', 'store_address'))
#   kyochon_tbl.to_csv('./data/kyochon.csv', encoding='cp949', mode='w', index=True)
#   print('------ 완료 ------')
#   del result[:]
#
#
# if __name__ == '__main__':
#   main()
