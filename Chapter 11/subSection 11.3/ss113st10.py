# Список делителей
#
# На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.
#
# Формат входных данных
# На вход программе подается натуральное число nn.
#
# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.

# put your python code here
n = int(input())
dl = []
for i in range (1, n+1) :
    if n%i == 0 : dl.append(i)
print(dl)