n = int(input())
if n <= 9:
    for i in range(1, n + 1):
        for g in range(1, i + 1):
            print(g, end = ' ')
        print(' ')
