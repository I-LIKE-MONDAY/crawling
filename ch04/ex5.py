# ch04/ex5.py
import matplotlib.pyplot as plt

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))
print(x)  # range(0, 4)

plt.bar(x, y1, width=0.7, color='blue')
plt.bar(x, y2, width=0.7, color='red', bottom=y1) # 막대그래프 두개를 쌓은 모양

plt.title('Quarterly Sales')
plt.xlabel('Quarters')
plt.ylabel('Sales')
xLabel = ['first', 'second', 'third', 'fourth']
plt.xticks(x, xLabel, fontsize=10)

plt.legend(['chairs', 'desks'])  # 범례

plt.show()

