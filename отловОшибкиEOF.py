number = int(input())
sum = 0
try:
    for i in range(3):
        number = int(input())
        sum+=number
except EOFError:
    print("Exception handled")
print(sum)
