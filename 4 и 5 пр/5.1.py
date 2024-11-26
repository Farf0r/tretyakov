s = input().split()
k = 0
for i in s:
    if i[0] == 'Е' or i[0] == 'е':
        k += 1
print(k)
