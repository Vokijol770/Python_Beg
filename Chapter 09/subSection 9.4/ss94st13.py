# Самый частотный символ
#
# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
#
# Формат входных данных
# На вход программе подается строка текста. Текст может содержать строчные и заглавные буквы английского и русского алфавита, а также цифры.
#
# Формат выходных данных
# Программа должна вывести символ, который появляется наиболее часто.
#
# Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
#
# Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.

# put your python code here
s = input()
abc = ""
count = 0
for c in s :
    if count <= s.count(c) :
        count = s.count(c)
        abc = c
    s = s.replace(c, '')
print(abc)