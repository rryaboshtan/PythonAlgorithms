# Алгоритм вычисления функций F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = n + 1 при n < 3,
# F(n) = F(n – 2) + n – 2, когда n ≥ 3 и четно,
# F(n) = F(n + 2) + n + 2, когда n ≥ 3 и нечетно.
# Сколько существует чисел n, для которых значение F(n) определено и будет пятизначным?

def f(n):
    if n < 3:
        return n + 1
    elif n >= 3 and n % 2 == 0:
        return f(n - 2) + n - 2
    elif n >= 3 and n % 2 != 0:
        return f(n + 2) + n + 2

n = 1
count = 0
while True:
    try:
        if len(str(f(n))) == 5:
            count+= 1
            print(count)
    except RecursionError:
        pass
    n += 1

# Result 216
