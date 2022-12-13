# naver_finance_crawler.py : 네이버 금융 국제증시 거래상위 100 기업 크롤링

import requests
from bs4 import BeautifulSoup

def get_top100(top100_url, top100_name):
  url = 'https://finance.naver.com/sise/sise_quant.nhn'
  result = requests.get(url)
  html = BeautifulSoup(result.content.decode('euc-kr', 'replace'), 'html.parser')
  top100 = html.find_all('a', {'class': 'tltle'})
  for i in range(100):
    url = 'http://finance.naver.com' + top100[i]['href']
    # print(url)
    top100_url.append(url)
    company_name = top100[i].string
    # print(company_name)
    top100_name.append(company_name)
  return (top100_url, top100_name)


def get_company(top100_name):
  company_name = input('주가를 검색할 기업이름을 입력하세요 >> ')
  for i in range(100):
    if company_name == top100_name[i]:
      return(i)

  if i == 100:
    print('입력한 기업은 거래상위 100 목록에 없습니다.')


# 검색한 기업 이름으로 url 크롤링링
def get_company_stockPage(company_url):
  result = requests.get(company_url)
  company_stockPage = BeautifulSoup(result.content, "html.parser")
  return company_stockPage

def get_price(company_url):
  company_stockPakage = get_company_stockPage(company_url)  # code3
  no_today = company_stockPakage.find('p', {'class': 'no_today'})
  blind = no_today.find('span', {'class': 'blind'})
  now_price = blind.text
  return now_price

def main():
  top100_url = []
  top100_name = []
  top100_url, top100_name = get_top100(top100_url, top100_name)

  print('현재 네이버 금융 거래 상위 100 기업 목록')
  print(top100_name)
  print()

  company = int(get_company(top100_name))
  if company == 100:
    print('입력한 기업은 거래 상위 100 목록에 없습니다.')
  else:
    now_price = get_price(top100_url[company])  # code 4
    print('%s 기업의 현재 주가는 %s 입니다.' % (top100_name[company], now_price))

if __name__ == '__main__':
  main()