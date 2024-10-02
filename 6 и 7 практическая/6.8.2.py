s = [1, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2]
n = []
k = 0
for i in s:
    k += 1
a = sum(s) // k
for i in s:
    if i != 0:
        n.append(i)
    else:
        n.append(a)
print(n)
