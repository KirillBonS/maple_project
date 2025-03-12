from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()#создание области размещения графика
ax = fig.gca(projection='3d')#создание сетки для 3х мерных фигур

# создание данных
X = np.arange(-2.5, 2.5, 0.1)#создание списка от -2.5 до 2.5 с шагом 0.1
Y = np.arange(-2.5, 2.5, 0.1)#создание списка от -2.5 до 2.5 с шагом 0.1
X, Y = np.meshgrid(X, Y)#создание прямоугольной сетки из массива значений x и массива значений y
Z = np.sin(Y*Y)*X#заданная функция

# построим поверхность
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
 linewidth=0, antialiased=False)#создание графика функции 

# настроим ось z
ax.set_zlim(-2.01, 2.01)#ограничение оси z
ax.zaxis.set_major_locator(LinearLocator(10))#разделение оси z на 10 промежутков
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))#форматный вывод чисел на оси z

# Добавим цветовую полосу, которая отображает значения в цвета
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
