def cal(a, b):
    r1 = a + b
    r2 = a - b
    r3 = a * b
    r4 = a / b
    return r1, r2, r3, r4

l, m, n, o = cal(7, 3)
print(f'{l}, {m}, {n}, {o}')