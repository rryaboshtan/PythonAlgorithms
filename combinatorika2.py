# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА

# Запишите слово, которое стоит на 350-м месте от начала списка.

# import itertools

# a = list(itertools.product('АКРУ', repeat=5))
# print(a[349])

word = 'АКРУ'
#Переводим это всё в четверичную систему счисления 0..3
def f(n):
    rezult = ''
    while n > 4:
        rezult += word[n % 4]
        n = n // 4
    rezult += word[n]
    #reverse result string
    return rezult[::-1]

print(f(349))

# Rezult КККУК

