# k-ая буква слова 🌶️🌶️
#
# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую
# букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число n, далее n строк, каждая на отдельной строке. В конце вводится натуральное
# число k – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.

# put your python code here
n = int(input())
ls = []
for _ in range(n) : ls.append(input())
k = int(input())
for c in ls :
    if len(c) >= k : print(c[k-1], end = "")