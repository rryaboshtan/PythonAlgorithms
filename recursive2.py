def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return F(n // 2)
    elif n % 2 != 0:
        return 1 + F(n - 1)

n = 0
while True:
    if (F(n) == 11):
        print(n)
        break
    n += 1 