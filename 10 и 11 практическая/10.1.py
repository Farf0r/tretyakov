a = open("ТДВ_УБ-42_vvod.txt").read()
a = [i.split() for i in a.split("\n")[:-1]]
print(a)

S = 0
k = 0

for i in a:
    for j in i:
        if a[i][j] > 0:
            S += a[i][j]
            k += 1

print(a)
