# Последовательность символов
#
# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
#
# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G
#
# Формат входных данных
#
# Формат выходных данных
# Программа должна вывести указанную последовательность символов.

# put your python code here
for _ in range(6) :
    print("AAA")
for _ in range(5) :
    print("BBBB")
print("E")
for _ in range(9) :
    print("TTTTT")
print("G")