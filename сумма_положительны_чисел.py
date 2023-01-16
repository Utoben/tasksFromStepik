# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.


f = [int(input()),int(input()),int(input())]

summ = 0

for i in (f):
    if i>0:
        summ+=i
print(summ)
