v = int(input())
k = int(input())
if v < 2 and k == 1:
    b = v - k + 1
elif k > v:
    b = k**2 + v**2
else:
    b = k**2 + v
print(b)
