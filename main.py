import numpy as np
from matplotlib import pyplot as plt
import toml

# Считываем данные из config.toml в переменные

with open('config.toml', 'r') as filestr:
    data = toml.load(filestr)
    xmin = float(data['xmin'])
    xmax = float(data['xmax'])
    step = float(data['step'])
    a = float(data['a'])
    b = float(data['b'])
    c = float(data['c'])

# Считаем и записываем вычисления

file = open('results.txt', 'w')
x = xmin
while x <= xmax:
    y = (a - x) * np.cos(b * x) + c
    file.write(str(y) + '\n')
    x += step
file.close()

# Выводим график на экран

x = np.linspace(int(xmin), int(xmax), int((xmax - xmin) / step + 1))
plt.plot(x, (a - x) * np.cos(b * x) + c)
plt.show()
