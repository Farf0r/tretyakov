def maxx():
    try:
        n = int(input())
        if n == 0:
            return 0
        else:
            a = maxx()
            return max(n, a)
    except ValueError:
        print("Введите число")
        return maxx()

b = maxx()
if b != 0:
    print(f"Наибольшее значение: {b}")