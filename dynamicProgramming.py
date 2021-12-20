# Максимальная сумма интервала (максимальная сумма интервала):
#  Если задана целочисленная последовательность длины n, a [1… n], найдите [1, n] определенный подинтервал [i, j] такой, что a [i] +… + a [j] и максимум
#  Например, (-2, 11, -4, 13, -5, 2) имеет максимальную сумму подсегмента 20, а подинтервал равен [2,4].

# Исчерпывающий метод сложность O(n ** 2)
def maxrange(a):
    n = len(a)
    sum = 0
    start = 0
    end = 0
    max = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + a[j]
            if (sum > max):
                max = sum
                start = i + 1
                end = j + 1
    print(start, end, max)

# Метод динамического программирования Сложность О(n)
def setSubSum(array, index):
    if sums[index - 1] >= 0:
        sums[index] = sums[index - 1] + array[i]
    else:
        sums[i] = array[i]


def getMaxSum(array):
    max = array[0]
    for i in range(1, len(array)):
        if max <= array[i]:
            max = array[i]

    return max

# Main program
array = [-2, 11, -4, 13, -5, 2]
sums = [0]*len(array)

for i in range(0, len(array)):
    setSubSum(array, i)

max = getMaxSum(sums)

maxrange(array)
print('Max sub sum is: ', max)