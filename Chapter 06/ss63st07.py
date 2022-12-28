# Квадратное уравнение 🌶️🌶️
#
# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# a*x^2+b*x+c=0.
# Формат входных данных
# На вход программе подается три вещественных числа a≠0, b, c, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
#
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

# put your python code here
from math import *
a, b, c = float(input()), float(input()), float(input())
D = b * b - 4 * a * c
if (D < 0) : print("Нет корней")
elif (D == 0) : print(-1 * b / 2 / a)
else :
    print(min((-1 * (b + sqrt(D)) / 2 / a), (-1 * (b - sqrt(D)) / 2 / a)))
    print(max((-1 * (b + sqrt(D)) / 2 / a), (-1 * (b - sqrt(D)) / 2 / a)))