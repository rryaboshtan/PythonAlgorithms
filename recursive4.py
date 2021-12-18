def F(n):
    if n < 2:
        return n
    elif n >= 2 and n % 2 == 0:
        return F(n // 2) + 1 
    elif n >= 2 and n % 2 != 0:
        return F(3 * n + 1) + 1

count = 0
for n in range(1, 101):
    if F(n) > 100:
        count += 1

print(count)
