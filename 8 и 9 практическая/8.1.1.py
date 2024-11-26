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
        print(a[i][j], end=' ')
    print()

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            S += a[i][j]
            k += 1

print('Сумма элементов над даигональю: ', S)

print('Количество положительных элементов над диагональю: ', k)
