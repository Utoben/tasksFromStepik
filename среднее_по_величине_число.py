# Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

x, y, z = [int(input()) for _ in range(3)]

if (x < y and x > z) or (x > y and x < z) :
    print(x)
elif (z < y and z > x) or (z > y and z < x):
    print(z)
elif (y < x and y > z) or (y > x and y < z):
    print(y)
else:
    print("Непонятно")

"""или 
# массив из 3 введенных чисел
a = [int(input()), int(input()), int(input())] 
# сортировка массива
a.sort()
# вывод среднего элемента массива
print(a[1])
# если поизвращаться, то можно и в одну строку,
# только нужно использовать функцию sorted(),
# которая не меняет изначальный массив а возвращает
# отсортированный дубликат.
# Выглядеть это будет так:
# print(sorted([int(input()), int(input()), int(input())])[1])
# ########################
или 
##########################
# import statistics
a = int(input())
b = int(input())
c = int(input())
list = [a, b, c]
print(statistics.median(list))
# 
# 
# """