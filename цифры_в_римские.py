a = int(input())

numbers = [1,2,3,4,5,6,7,8,9,10]
roman_numbers = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}

if a not in numbers:
    print('ошибка')
else:
    for key, value in roman_numbers.items():
        if key == a:
            roman_numbers[key]=value
            print(value)





