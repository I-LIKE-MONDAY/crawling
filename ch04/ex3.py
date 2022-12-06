# ch04/ex3.py
import pandas as pd

data_dic = {
  'year': [2018, 2019, 2020],
  'sales': [350, 480, 1099]
}
print(data_dic)  # {'year': [2018, 2019, 2020], 'sales': [350, 480, 1099]}

df1 = pd.DataFrame(data_dic)  # 데이터를 틀에 맞게 가공해줌
print(df1)
#      year  sales
#   0  2018    350
#   1  2019    480
#   2  2020   1099

data2 = ['1반', '2반', '3반', '4반', '5반']
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   index=['중간고사', '기말고사'], columns=data2[0:3])
print(df2)
#              1반    2반    3반
#     중간고사  89.2  92.5  90.8
#     기말고사  92.8  89.9  95.2

data_df = [['20201101', 'Hong', '90', '95'],
           ['20201102', 'Kim', '93', '94'],
           ['20201103', 'Lee', '87', '97']]

df3 = pd.DataFrame(data_df)
print(df3)
#               0     1   2   3
#     0  20201101  Hong  90  95
#     1  20201102   Kim  93  94
#     2  20201103   Lee  87  97

df3.columns = ['학번', '이름', '중간고사', '기말고사']  # df3에 컬럼 추가
print(df3)
#        학번    이름 중간고사 기말고사
#     0  20201101  Hong   90   95
#     1  20201102   Kim   93   94
#     2  20201103   Lee   87   97

print(df3.head(2))  # 위에서 2행 출력
print(df3.tail(2))  # 밑에서 2행 출력

print(df3['이름'])
#   0    Hong
#   1     Kim
#   2     Lee

df3.to_csv('./data/score.csv', header=True, encoding='utf-8-sig')
df3.to_csv('./data/score1.csv', header=False, encoding='utf-8-sig')

df4 = pd.read_csv('./data/score.csv', encoding='utf-8', index_col=0)
print(df4)
#          학번    이름  중간고사  기말고사
#     0  20201101  Hong    90    95
#     1  20201102   Kim    93    94
#     2  20201103   Lee    87    97

df5 = pd.read_csv('./data/score.csv', encoding='utf-8', index_col='학번')
print(df5)
#                  0    이름  중간고사  기말고사
# 학번
# 20201101           0  Hong    90    95
# 20201102           1   Kim    93    94
# 20201103           2   Lee    87    97

