n = int(input('Введите значение n: '))
for i in range(1, n + 1):
    stri = str(i)
    a = True
    for j in stri:
        if j == '0' or i % int(j) != 0:
            a = False
            break
    if a == True:
        print(i)