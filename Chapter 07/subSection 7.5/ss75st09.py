# Одинаковые цифры
#
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

# put your python code here
n = int(input())
s = "YES"
while (9 < n) :
    t = n % 10
    if ((n % 100) // 10 != t) :
        s = "NO"
        n = 0
    n = n // 10
print(s)