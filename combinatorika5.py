# Сколько существует 6-значных чисел, делящихся на 5, в которых каждая цифра может
# встречаться только один раз, при этом никакие две чётные и две нечётные 
# цифры не стоят рядом

import itertools

a = list(itertools.permutations('0123456789', r=6))

forbiddens = list(itertools.permutations('13579', r = 2)) + list(itertools.permutations('02468', r = 2))

count = 0
for x in a:
    s = ''.join(x)
    if s[0] != '0' and (s[-1] == '5' or s[-1] == '0'):
        for forbidden in forbiddens:
            s1 = ''.join(forbidden)
            if s1 in s:
                break
        else: 
            count += 1

print(count)

# Result 1296
