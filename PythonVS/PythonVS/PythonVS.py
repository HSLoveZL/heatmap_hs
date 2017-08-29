import csv
import numpy as np
import matplotlib.pyplot as plt

arr = []
with open('D:\\UnityConsole\\2DCoordinate\\2017-08-13\\test.csv') as f:
	f_csv = csv.reader(f)
	for value in f_csv:
		arr.append(value)

x = []
y = []
for values in arr[1:]:
	axisX = float(values[0])
	axisY = float(values[1])
	x.append(axisX)
	y.append(axisY)

heat_map, xedges, yedges = np.histogram2d(x, y, bins=16)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.axis('off')
plt.imshow(heat_map.T, interpolation='sinc', extent=extent, cmap=plt.cm.get_cmap('rainbow', 1000), aspect='auto', origin='lower')
plt.savefig(".\\resultsPic\\2017-08-26ht.png", dpi=160)
