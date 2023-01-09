# Численный треугольник 1
#
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
#
# 1
# 22
# 333
# 4444
# 55555
# ...
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.
#
# Примечание. Используйте вложенный цикл for.

# put your python code here
n = int(input())
for i in range(1, n+1) :
    print(str(i)*i)