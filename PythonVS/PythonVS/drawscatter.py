import csv
import numpy as np
import matplotlib.pyplot as plt

arr = []
with open('D:\\UnityConsole\\test006.csv') as f:
	f_csv = csv.reader(f)
	for value in f_csv:
		arr.append(value)

x = []
y = []
for val in arr[1:]:
	axisX = float(val[0])
	axisY = float(val[1])
	x.append(axisX)
	y.append(axisY)
	
	plt.scatter(x, y, s=20, alpha=0.8)
	plt.plot(x[0:], y[0:], 'r')
plt.xlim(xmin=np.min(x), xmax=np.max(x))
plt.ylim(ymin=np.min(y), ymax=np.max(y))
# plt.xlim(xmin=-3, xmax=3)
# plt.ylim(ymin=0, ymax=5)
plt.savefig(".\\resultsPic\\testsp006.png", dpi=160, transparent=True)
