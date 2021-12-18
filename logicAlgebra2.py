# На числовой прямой даны три отрезка: P = [10, 40], Q = [5, 15] и R = [35, 50]. Какова наименьшая возможная длина промежутка A, что формула
# ((x ∈ А) ∨ (x ∈ P)) ∨ ((x ∈ Q)→ (x ∈ R))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

p1, p2, q1, q2, r1, r2 = 10, 40, 5, 15, 35, 50
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
R = [i / 10 for i in range(r1 * 10, r2 * 10 + 1)]


def f(x, A):
    return ((x in A) or (x in P)) or ((x in Q) <= (x in R))


A = set()
for x in [i / 10 for i in range(10, 600)]:
    if not f(x, A):
        A.add(x)

print(sorted(A))

# Result 5
