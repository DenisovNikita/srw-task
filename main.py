from math import factorial as f


def binom(n, k):
    return f(n) // (f(k) * f(n - k))


p = 0.05
q0 = 0.05
q1 = 0.05


def get_A_kt(k, t):
    s = 0
    for q in range(t, k + 1):
        s += binom(k, q) * (1 - q1) ** q * q1 ** (k - q)
    return p * s


def get_B_kt(k, t):
    s = 0
    for q in range(t, k + 1):
        s += binom(k, q) * q0 ** q * (1 - q0) ** (k - q)
    return (1 - p) * s


n = 10
x = 0.6

opt_k, opt_t, opt_pr = 0, 0, 0
for k in range(1, n + 1):
    for t in range(1, k + 1):
        num = get_A_kt(k, t)
        denum = get_A_kt(k, t) + get_B_kt(k, t)
        pr = num / denum
        if pr > opt_pr:
            opt_k, opt_t, opt_pr = k, t, pr
        print(f"k = {k}, t = {t}, pr = {pr}")
print(f"opt_k = {opt_k}, opt_t = {opt_t}, opt_pr = {opt_pr}")
