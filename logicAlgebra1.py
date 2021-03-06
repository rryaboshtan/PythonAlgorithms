# На числовой прямой даны два отрезка: P = [2, 10] и Q = [6, 14]. Какова наибольшая возможная длина интервала A, что формула
# ((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2 = 2, 10, 6, 14
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)

A = set([i / 10 for i in range(10, 201)])
for x in [i / 10 for i in range(10, 201)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# Result 12