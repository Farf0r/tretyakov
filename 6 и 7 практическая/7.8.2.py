s = int(input('Введите длину массима: '))


def zamena(x):
    a = x[0]
    x[0] = x[-1]
    x[-1] = a


t = []
for i in range(s):
    print('Введите ', i, 'элемент массива')
    t.append(int(input()))
print(t)
zamena(t)
print(t)
