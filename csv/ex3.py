# csv/ex3.py
import os, re
import usecsv as uc

os.chdir(r'.\data')

apt = uc.switch(uc.opencsv('apt_202210.csv'))

new_list = []
for i in apt:
  try:
    # 부산의 크기가 150이 넘거나 5억 이상인 리스트 저장
    if re.match('부산광역시', i[0]):
      if i[5] >= 150:
        new_list.append([i[0], i[4], i[-4]])
      elif i[-7] >= 50000:
        new_list.append([i[0], i[4], i[-4]])
  except:
    pass

print(len(new_list))
uc.writecsv('over120_lower300003.csv', new_list)