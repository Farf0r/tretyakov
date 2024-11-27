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
print(" ")

def perev(a):
    lines = len(a)
    columns = len(a[0])
    x = [[0] * lines for i in range(columns)]
    for i in range(lines):
        for j in range(columns):
            x[j][i] = a[i][j]
    return x

c = perev(a)
for i in c:
    print(i)
