# Ревью кода - 7 🌶️
#
# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа
# или 0, если чётных цифр в записи нет. Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только
# одну строку и может быть исправлена без изменения других строк.
#
# Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.

# put your python code here
n = int(input())
s = 0
while n > 1:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)