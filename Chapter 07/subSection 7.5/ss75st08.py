# Вторая цифра
#
# Дано натуральное число n (n > 9). Напишите программу, которая определяет его вторую (с начала) цифру.
#
# Формат входных данных
# На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.
#
# Формат выходных данных
# Программа должна вывести его вторую (с начала) цифру.

# put your python code here
n = int(input())
while (n > 9) :
    t= n%10
    n = n // 10

print(t)