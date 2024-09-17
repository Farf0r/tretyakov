a = int(input())
count = 0
for i in range(2, a // 2 + 1):
    if a % i == 0:
        count += 1
if count <= 0:
    print('Простое')
else:
    print('Не простое')
