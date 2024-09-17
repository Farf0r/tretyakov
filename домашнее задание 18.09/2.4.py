v = int(input())
k = int(input())
if v < k:
    z = v - k + 1
elif k > v:
    z = k**2 - v**2
else:
    z = k**2 - k
print(z)


