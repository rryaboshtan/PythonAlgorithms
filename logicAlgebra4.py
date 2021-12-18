# ((x ∈ А) → (x**2 <= 81)) ∧ ((y**2 <= 36) →(y ∈ A))
# тождественно истинно при любых вещественных x и y. 
# Какую наибольшую длину может иметь отрезок А?
import itertools

def f(x, y, A):
    return ((x in A) <= (x * x <= 81)) and ((y * y <= 36) <= (y in A))

A = set(range(-10, 10))
for x, y in itertools.product(range(-10, 10), repeat = 2):
    if not f(x, y, A):
        A.remove(x)

print(sorted(A))

# Result 18