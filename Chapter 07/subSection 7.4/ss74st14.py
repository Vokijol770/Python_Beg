# Ведьмаку заплатите чеканной монетой
#
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не
# принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
#
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
#
# Формат входных данных
# На вход программе подается одно натуральное число, цена за услугу ведьмака.
#
# Формат выходных данных
# Программа должна вывести минимально возможное количество чеканных монет для оплаты.
#
# Интересное решение
# n = int(input())
# k = 0
# for i in (25, 10, 5, 1):
#     while n // i > 0:
#         k += 1
#         n -= i
# print(k)

# put your python code here
count = 0;
n = int(input())
while(0 != n) :
    if 25 <= n :
        count += 1
        n -= 25
    elif 10 <= n :
        count += 1
        n -= 10
    elif 5 <= n :
        count += 1
        n -= 5
    else :
        count += 1
        n -= 1
print(count)