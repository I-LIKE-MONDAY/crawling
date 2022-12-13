# ch06/ex1.py
from bs4 import BeautifulSoup as bs

html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'

soup = bs(html, 'html.parser')

# tag_h1 = soup.h1
# print(tag_h1)
#
# tag_div = soup.div
# print(tag_div)
#
# tag_ul = soup.ul
# print(tag_ul) # ul 태그 2개인데 제일 앞의 태그만 나옴
#
# tag_a = soup.a
# print(tag_a)  # a 태그 3개인데 제일 앞의 태그만 나옴
#
# tag_ul_all = soup.find_all('ul')
# print(tag_ul_all) # 리스트로 리턴이 되면서 전체 ul 값이 들어옴
#
# for tag_ul in tag_ul_all:
#   print('## %s' % tag_ul)
#
# tag_a_all = soup.find_all('a')
# for tag_a in tag_a_all:
#   print('## %s' % tag_a)

# tag_a = soup.a
# print(tag_a.attrs)
# print(tag_a['href'])
# print(tag_a['class'])

# tag_ul2 = soup.fnd('ul', attrs={'class':'brand'})  # find : 제일 처음꺼 하나만 가져옴
# print(tag_ul2)

# title = soup.find(id = 'title')
# print(title)
# print(title.string)

li_list = soup.select('div > ul.brand > li')
print(li_list)

for li in li_list:
  print(li.string)
