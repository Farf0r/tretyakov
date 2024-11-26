n = int(input())
a = []
S = 0
k = 0

for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)

print("Изначальный массив: ")

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

print(" ")

max1 = []
min1 = []
for i in range(n):
    max1.append(max(a[i]))
for i in range(n):
    min1.append(min(a[i]))

print(max1,min1)

print("Конечный массив: ")

