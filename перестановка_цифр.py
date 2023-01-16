# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: abc, \, acb, \, bac, \, bca, \, cab, \, cbaabc,acb,bac,bca,cab,cba.
num = int(input())

digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(str(digit1)+str(digit2)+str(digit3))
print(str(digit1)+str(digit3)+str(digit2))
print(str(digit2)+str(digit1)+str(digit3))
print(str(digit2)+str(digit3)+str(digit1))
print(str(digit3)+ str(digit1)+str(digit2))
print(str(digit3)+str(digit2)+str(digit1))