# ch04/nvCrawler.py
# numpy 사용해보기(교재 110p)
import numpy as np

# print(np.__version__)

ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)  # [1 2 3 4 5]
print(type(ar1))  # <class 'numpy.ndarray'>

ar2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(ar2)

ar3 = np.arange(1, 11, 2)  # 1에서 11까지의 범위, 증가값 2 (리스트로 리턴)
print(ar3)  # [1 3 5 7 9]

ar4 = np.arange(1, 31, 3)  # 1에서 31까지의 범위, 증가값 3 (리스트로 리턴)
print(ar4)  # [ 1  4  7 10 13 16 19 22 25 28]

ar5 = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)  # 3행 2열로 출력
print(ar5)  # [[1 2]
            # [3 4]
            # [5 6]]

ar6 = np.zeros((2, 3))  # 0값을 2행 3열로 출력
print(ar6)  # [[0. 0. 0.]
            # [0. 0. 0.]]

ar7 = np.array([[10, 20, 30], [40, 50, 60]])
ar8 = ar7[0:2, 0:2] # 0:2에서 0은 인덱스 번호, 2는 가져올 개수
print(ar8)  # [[10 20]
            # [40 50]]

ar9 = ar7[0:]
print(ar9)  # [[10 20 30]
            # [40 50 60]]

ar10 = ar7[0, :]  # index 0번째 데이터만 다 가져오기
print(ar10) # [10 20 30]

ar11 = np.array(([1, 2, 3, 4, 5]))
ar12 = ar11 + 10  # 배열 내부의 각 데이터에 10씩 더함
print(ar12)  # [11 12 13 14 15]

ar13 = ar11 + ar12  # [1, 2, 3, 4, 5] + [11 12 13 14 15]
print(ar13)  # [12 14 16 18 20]

ar14 = ar13 * 2  # [12 14 16 18 20] * 2
print(ar14) # [24 28 32 36 40]

