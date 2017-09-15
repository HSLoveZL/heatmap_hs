# -*-coding-*-
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [0.1, 0.2, 0.3, 0.4, 0.5]

intensity = [
    [5, 10, 15, 20, 25],
    [30, 35, 40, 45, 50],
    [55, 60, 65, 70, 75],
    [80, 85, 90, 95, 100],
    [105, 110, 115, 120, 125]
]
x, y = np.meshgrid(x, y)

intensity = np.array(intensity)

plt.pcolormesh(x, y, intensity)
plt.colorbar()
plt.show()
