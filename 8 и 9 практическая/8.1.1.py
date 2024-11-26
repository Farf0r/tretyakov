n = int(input())
a = []
S = 0
k = 0
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)

print('Изначальный массив: ')

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

for i in range(n):
    for j in range(n):
        if a[j] > a[i]:
            S += a[i][j]

print('Сумма элементов над даигональю: ', S)

for i in range(n):
    for j in range(n):
        if a[i][j] > 0:
            k += 1

print('Количество положительных элементов над диагональю: ', k)