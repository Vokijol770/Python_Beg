# Простые числа
#
# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все простые числа от a до b включительно.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести все простые числа от a до b включительно, каждое на отдельной строке.
#
# Примечание. Число 1 простым не является.

# put your python code here
a, b = int(input()), int(input())
for i in range(a, b+1) :
    count = 0
    for j in range(1, i+1) :
        if i%j == 0 : count += 1
    if count < 3 and i != 1 : print(i)