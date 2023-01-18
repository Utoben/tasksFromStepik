num = int(input())

full_month_dict = {1:'january', 3:'march', 5:'may', 7:'july', 8:'august', 10:'october', 12:'december'}
not_full_month_dict = {4:'april', 6:'june', 9:'september', 11:'november'}
feb_dict = {2:'february'}

a = num in full_month_dict

if a == True:
    print('31')
    
b = num in not_full_month_dict

if b == True:
    print('30')
    
b = num in feb_dict

if b == True:
    print('28')