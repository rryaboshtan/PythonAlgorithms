def findMaxIndex(permutation):
    for i in range(len(permutation) - 2, -1, -1):
        if permutation[i] < permutation[i + 1]:
            return i
    return -1

def findIndexOfBiggerElement(permutation, element):
    for i in range(len(permutation) - 1, -1, -1):
        if permutation[i] > element:
            return i
    return -1

def swap(permutation, i, j):
    permutation[i], permutation[j] = permutation[j], permutation[i]

def reversePermutation(permutation, index):
    n = len(permutation)
    permutation = permutation[:index + 1:] + permutation[n - 1:index:-1]
    return permutation

def permutationGenerator(n):
    permutation = list(range(1, n + 1))
    print(permutation)
    index = findMaxIndex(permutation)
    while index != -1:
        element = permutation[index]
        swapIndex = findIndexOfBiggerElement(permutation, element)
        swap(permutation, index, swapIndex)
        permutation = reversePermutation(permutation, index)
        print(permutation)
        index = findMaxIndex(permutation)

permutationGenerator(3)
