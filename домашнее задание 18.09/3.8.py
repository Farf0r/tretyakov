a = int(input())
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,]
if 1 <= a <= 12:
    print(b[a - 1])
else:
    print('Такого месяца нету')
