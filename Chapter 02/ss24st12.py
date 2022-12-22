# Арифметическая прогрессия
#
# Арифметической прогрессией называется последовательность чисел a1,a2,...,an, каждое из которых, начиная с a2,
# получается из предыдущего прибавлением к нему одного и того же постоянного числа d(разность прогрессии), то есть:
#
# an=an−1+d
#
# Если известен первый член прогрессии и её разность, то n-ый член арифметической прогрессии находится по формуле:
#
# an=a1+d*(n−1)
#
# Входные данные
# На вход программе подаётся три целых числа: a1, d и n, каждое на отдельной строке.
#
# Выходные данные
# Программа должна вывести n-ый член арифметической прогрессии.

# put your python code here
a, d, n = int(input()), int(input()), int(input())
print(a + d * (n-1))