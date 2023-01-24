a1, b1,a2, b2 = [int(input()) for _ in range(4)]

if (b1 == a2):
    print(b1)
elif (b2 == a1):
    print(b2)
elif (b1 < a2 or b2 < a1):
    print("пустое множество")
else:
    print(max(a1, a2), min(b1, b2))