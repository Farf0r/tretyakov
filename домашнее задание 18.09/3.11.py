a = int(input('Введите ваш возраст '))
if a % 10 == 1:
    print('Вам ', a, ' год')
elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    print('Вам ', a, ' года')
elif a % 10 == 5 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9:
    print('Вам ', a, ' лет')
elif a % 100 == 10 or a % 100 == 11 or a % 100 == 12 or a % 100 == 13 or a % 100 == 14 or\
     a % 100 == 15 or a % 100 == 16 or a % 100 == 17 or a % 100 == 18 or a % 100 == 19 or\
     a % 100 == 20:
    print('Вам ', a, ' лет')
