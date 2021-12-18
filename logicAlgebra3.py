# На числовой прямой даны три отрезка: P = [7, 14], Q = [9, 11]. Укажите наибольшую возможную длину промежутка A, для которого формула
# ((x ∈ P) ~ (x ∈ Q)) → !(x ∈ A))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2 = 7, 14, 9, 11
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]


def f(x, A):
    return ((x in P) == (x in Q)) <= (not x in A)


A = set([i / 10 for i in range(10, 201)])
for x in [i / 10 for i in range(10, 201)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# Numbers 9,  10 and 11 are excluded from the array
# Result 3
