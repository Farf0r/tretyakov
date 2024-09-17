x = int(input())
y = int(input())
if x < 2 and y == 2:
    b = x * y + 1
elif x > y:
    b = y**2 + x**2
else:
    b = x**2 + 2
print(b)
