a = int(input())
if a > -1 and a < 17:
    print('Принадлежит')
else:
     print('Не принадлежит')


if (a>-30) and (a <= -2) or (a > 7)and(a<=25):
    print('Принадлежит')
else:
     print('Не принадлежит')     

n = int(input())
print("YES" if((n % 7 == 0 or n % 17 == 0) and 1000 <= n <= 9999) else 'NO')