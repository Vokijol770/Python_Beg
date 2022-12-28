# Евклидово расстояние
#
# На плоскости евклидово расстояние между двумя точками (x1; y1) и (x2; y2) определяется так ρ=sqrt((x1−x2)^2+(y1−y2)^2)
#
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
#
# Формат входных данных
# На вход программе подается четыре вещественных числа, каждое на отдельной строке – x1, y1, x2, y2.
#
# Формат выходных данных
# Программа должна вывести одно число – евклидово расстояние.

# put your python code here
from math import sqrt
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt((x1-x2)**2+(y1-y2)**2))