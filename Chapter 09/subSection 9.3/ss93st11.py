# Нижний регистр
#
# На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
#
# Формат входных данных
# На вход программе подается строка.
#
# Формат выходных данных
# Программа должна вывести количество буквенных символов в нижнем регистре.

# put your python code here
s = input()
slov = "abcdefghijklmnopqrstuvwxyz"
count = 0
for c in s :
    if c in slov : count += 1
print(count)