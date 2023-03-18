from math import *

def p1(x):
    return -3 * x

def q1(x):
    return 2

def f1(x):
    return 1.5

def p2(x):
    return 1

def q2(x):
    return 0

def f2(x):
    return 4 * x + 4

def p3(x):
    return -2

def q3(x):
    return -3

def f3(x):
    return 0

def sweep_bound(p, q, f, a, b, sigma1, gamma1, delta1, sigma2, gamma2, delta2, n):
    h = (b - a) / n
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    alpha = [0] * n
    beta = [0] * n
    ans = []
    x[0] = a
    x[n] = b
    alpha[0] = -gamma1 / (h * sigma1 - gamma1)
    beta[0] = delta1 / (sigma1 - gamma1 / h)

    for i in range(n - 1):
        x[i + 1] = x[i] + h
        vr_h = h ** (-2)
        vr_p = p(x[i + 1]) / (2 * h)
        A = vr_h - vr_p
        B = vr_h + vr_p
        C = -2 * vr_h + q(x[i + 1])
        alpha[i + 1] = -B / (A * alpha[i] + C)
        beta[i + 1] = (f(x[i + 1]) - A * beta[i]) / (A * alpha[i] + C)

    y[n] = (h * delta2 + gamma2 * beta[n - 1]) / (h * sigma2 + gamma2 * (1 - alpha[n - 1]))

    for i in range(n, 0, -1):
        y[i - 1] = y[i] * alpha[i - 1] + beta[i - 1]

    for i in range(n + 1):
        ans.append([x[i], y[i]])

    return ans

#основная программа
print("Solution of the boundary value problem by the sweep method according to the variant:")
print(*sweep_bound(p1, q1, f1, 0.7, 1, 0, 1, 1.3, 0.5, 1, 2, 20), sep='\n')
print()

print("Solution of the boundary value problem by the sweep method own version number 1:")
print(*sweep_bound(p2, q2, f2, 0, 1, 1, 0, 0, 0, 1, 4, 20), sep='\n')
print()

print("Solution of the boundary value problem by the sweep method own version number 2:")
print(*sweep_bound(p3, q3, f3, -1, 0, 1, 0, e ** (-3), 0, 1, 3, 20), sep='\n')

















