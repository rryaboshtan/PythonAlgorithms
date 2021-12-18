# Алгоритм вычисления функции F(n), где n – целое число, задан следующими соотношениями:
# F(n) = n, при n(5,
# F(n)=n + F(n / 2 – 3), когда n > 5 и делится на 8,
# F(n)=n + F(n + 4), когда n > 5 и не делится на 8.
# Назовите максимальное значение n, для которого возможно вычислить F(n).
def F(n):
    if n <= 5:
        return n
    elif n > 5 and n % 8 == 0:
        return n + F(n // 2 - 3)
    elif n > 5 and n % 8 != 0:
        return n + F(n + 4)


n = 1
print('f  n')
while True:
    try:
        print(F(n), n)
    except RecursionError:
        pass
    n += 1

# result
# f  n
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 9 8
# 33 12
# 21 16
