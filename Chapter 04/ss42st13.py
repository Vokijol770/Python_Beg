# Високосный год
#
# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным,
# то выведите «YES», иначе выведите «NO».
#
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
year = int(input())
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("YES")
else:
    print("NO")