# csv/usecsv.py


# 파일 오픈 함수
import csv, os, re

def opencsv(filename):  # 파일 읽어와서 리스트로 리턴해주는 함수
  f = open(filename, 'r')
  reader = csv.reader(f)
  output = []
  for i in reader:
    output.append(i)
  return output

# 파일 쓰기 함수
def writecsv(filename, the_list):
  # 파일 읽을때 사용 : with open
  with open(filename, 'w', newline='') as f:
    a = csv.writer(f, delimiter=',')  # 구분자
    a.writerows(the_list)  # 한 줄씩 저장

# 문자 리스트 -> 실수 리스트 변환
# a = [['1','2','3'],['2','3',5']]
# b = switch(a)
# b = [[1.0,2.0,3.0],[2.0,3.0,5.0]]
def switch(listName):
  for i in listName:
    for j in i:
      try:
        i[i.index(j)] = float(re.sub(',', '', j))  # 콤마(,) 를 빈 값( ) 으로 변환
      except:
        pass
  return listName




