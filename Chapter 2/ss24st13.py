# Разделяй и властвуй
#
# Напишите программу, которая считывает целое положительное число x и выводит на экран последовательность чисел
# x,2*x,3*x,4*x и 5*x, разделённых тремя черточками.
#
# Формат входных данных
# На вход программе подаётся целое положительное число.
#
# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.

# put your python code here
a = int(input())
print(a, 2*a, 3*a, 4*a, 5*a, sep = "---")