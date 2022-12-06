# ch04/ex2.py
# pandas 사용해보기

import pandas as pd

print(pd.__version__)

data1 = [10, 20, 30, 40, 50]

data2 = ['1반', '2반', '3반', '4반', '5반']

sr1 = pd.Series(data1)  # Series 자료형
print(sr1)  # 0    10
            # 1    20
            # 2    30
            # 3    40
            # 4    50
            # dtype: int64

sr2 = pd.Series(data2)
print(sr2)  # 0    1반
            # 1    2반
            # 2    3반
            # 3    4반
            # 4    5반
            # dtype: object


sr3 = pd.Series([101, 102, 103, 104, 105])
sr4 = pd.Series(['월', '화', '수', '목', '금'])

sr5 = pd.Series(data1, index=[1001, 1002, 1003, 1004, 1005])  # 인덱스 값 지정 가
print(sr5)    # 1001    10
              # 1002    20
              # 1003    30
              # 1004    40
              # 1005    50
              # dtype: int64

sr6 = pd.Series(data1, index=data2)
print(sr6)  # 1반    10
            # 2반    20
            # 3반    30
            # 4반    40
            # 5반    50
            # dtype: int64

sr7 = pd.Series(data2, index=data1)
print(sr7)      # 10    1반
                # 20    2반
                # 30    3반
                # 40    4반
                # 50    5반
                # dtype: object


sr8 = pd.Series(data2, index=sr4)
print(sr8)    # 월    1반
              # 화    2반
              # 수    3반
              # 목    4반
              # 금    5반
              # dtype: object

print(sr8[2]) # 자리값 inde의 값 : 3반
print(sr8['수']) # 지정한 index의 값: 3반
print(sr8[-1]) # 뒤에서 첫번째 인덱스의 값 : 5반
print(sr8[0:4]) # 월    1반
                # 화    2반
                # 수    3반
                # 목    4반

print(sr8.values) # ['1반' '2반' '3반' '4반' '5반']

print(sr1 + sr3)
# 0    111
# 1    122
# 2    133
# 3    144
# 4    155
# dtype: int64

print(sr4 + sr2)
# 0    월1반
# 1    화2반
# 2    수3반
# 3    목4반
# 4    금5반
# dtype: object

