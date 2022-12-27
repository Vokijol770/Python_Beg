# Красивое число 🌶️
#
# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу,
# определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым,
# или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
n = int(input())
if ((1000 <= n < 10000) and ((n % 7 == 0) or (n % 17 == 0))):
    print("YES")
else:
    print("NO")