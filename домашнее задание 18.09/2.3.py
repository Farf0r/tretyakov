a = int(input())
b = int(input())
if a < b:
    c = a + b
elif a > b and a > 3:
    c = b**2 - b
else:
    c = b**2 - 1
print(c)
