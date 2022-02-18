from math import factorial as f


def binom(n, k):
    return f(n) // (f(k) * f(n - k))


def get_value(k, q, p):
    return p ** (k - q + 1) * (1 - p) ** q - p ** q * (1 - p) ** (k - q + 1)


n = 100

p = 0.05
opt_k, opt_t, opt_s = 0, 0, 0
for k in range(1, n):
    for t in range(1, k + 1):
        s = 0
        for q in range(t, k + 1):
            s += binom(k, q) * get_value(k, q, p)
        if s > opt_s:
            opt_k, opt_t, opt_s = k, t, s
        print(f"k = {k}, t = {t}, s = {s}\n")
print(f"opt_k = {opt_k}, opt_t = {opt_t}, opt_s = {opt_s}\n")
