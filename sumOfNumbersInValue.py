# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input())

last_digit = num % 10
third_digit = (num // 10)% 10
second_digit = (num // 100)%10
first_digit = num // 1000

if (first_digit+last_digit)==(second_digit-third_digit):
    print("ДА")
else:
    print("НЕТ")