chet = []
nechet = []
a = input('Введите целое число ')
for i in a:
    if int(i) % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
print(chet, nechet)
        
