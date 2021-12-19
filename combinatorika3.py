# Женя составляет слова переставляя буквы З, А, П, И, С, Ь. 
# Сколько слов может составить Женя, если известно, 
# что Ь не может стоять на первом месте и после гласной?

import itertools

a = list(itertools.permutations('ЗАПИСЬ', r=6))

count = 0
for x in a:
    f = ['АЬ','ИЬ']
    if x[0] != 'Ь':
        s = ''.join(x)
        for forbidden in f:
            if forbidden in s:
                break
        else:
            count += 1

print(count)