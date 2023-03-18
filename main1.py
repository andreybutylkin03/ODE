from math import *
from copy import *

def function_pull (uk, x, y):                       # задача уравнений
    if uk == 1:
        return (y - y ** 2) * x                     # уравнение по варианту
    elif uk == 2:
        return 2 * x + 3 * x ** 2                   # свой пример
    else:
        print("error")

def function_pull_sys (uk, x, y):              # уравнения для системы
    if uk == 1:
        return x + y[0] - y[1] ** 2 + 2
    elif uk == 2:
        return sin(x - y[0]) + 2.1 * y[1]
    else:
        print("error")

def runge_kutt_2 (uk, len_ab, n, x, y):             # метод Рунге-Кутта
    h = len_ab / n                                  # второго порядка точности
    h_p = h / 2                                     # для ОДУ
    ans = []
    ans.append([x, y])
    for i in range(n):
        f_prev = function_pull(uk, x, y)
        f_now = function_pull(uk, x + h, y + h * f_prev)
        y = y + h_p * (f_prev + f_now)
        x = x + h
        ans.append([x, y])
    return ans

def runge_kutt_4 (uk, len_ab, n, x, y):             # метод Рунге-Кутта
    h = len_ab / n                                  # четвертого порядка точности
    h_p = h / 2                                     # для ОДУ
    ans = []
    ans.append([x, y])
    for i in range(n):
        k1 = function_pull(uk, x, y)
        k2 = function_pull(uk, x + h_p, y + h_p * k1)
        k3 = function_pull(uk, x + h_p, y + h_p * k2)
        k4 = function_pull(uk, x + h, y + h * k3)
        y = y + h_p * (k1 + 2 * k2 + 2 * k3 + k4) / 3
        x = x + h
        ans.append([x, y])
    return ans

def runge_kutt_2_sys (uk_ar, len_ab, n, x, y):      # метод Рунге-Кутта
    h = len_ab / n                                  # второго порядка точности
    h_p = h / 2                                     # для системы ОДУ
    ans = []
    ans.append([x, deepcopy(y)])
    kol_func = len(uk_ar)
    for i in range(n):
        y_prev = deepcopy(y)
        for j in range(kol_func):
            f_prev = function_pull_sys(uk_ar[j], x, [y_prev[k] for k in range(kol_func)])
            f_now = function_pull_sys(uk_ar[j], x + h, [y_prev[k] + h * f_prev for k in range(kol_func)])
            y[j] = y[j] + h_p * (f_prev + f_now)
        x = x + h
        ans.append([x, deepcopy(y)])
    return ans

def runge_kutt_4_sys (uk_ar, len_ab, n, x, y):      # метод Рунге-Кутта
    h = len_ab / n                                  # четвертого порядка точности
    h_p = h / 2                                     # для ОДУ
    ans = []
    ans.append([x, deepcopy(y)])
    kol_func = len(uk_ar)
    for i in range(n):
        y_prev = deepcopy(y)
        for j in range(kol_func):
            k1 = function_pull_sys(uk_ar[j], x, [y_prev[k] for k in range(kol_func)])
            k2 = function_pull_sys(uk_ar[j], x + h_p, [y_prev[k] + h_p * k1 for k in range(kol_func)])
            k3 = function_pull_sys(uk_ar[j], x + h_p, [y_prev[k] + h_p * k2 for k in range(kol_func)])
            k4 = function_pull_sys(uk_ar[j], x + h, [y_prev[k] + h * k3 for k in range(kol_func)])
            y[j] = y[j] + h_p * (k1 + 2 * k2 + 2 * k3 + k4) / 3
        x = x + h
        ans.append([x, deepcopy(y)])
    return ans

# основная программа
print("ODE solution according to the variant:")
print("~Second order~")
print(*runge_kutt_2(1, 3, 15, 0, 3), sep='\n')
print()
print("~Fourth order~")
print(*runge_kutt_4(1, 3, 15, 0, 3), sep='\n')
print()

print("ODE solution own example:")
print("~Second order~")
print(*runge_kutt_2(2, 2, 10, 0, 0), sep='\n')
print()
print("~Fourth order~")
print(*runge_kutt_4(2, 2, 10, 0, 0), sep='\n')
print()

print("Solution of the ODE system according to the variant:")
print("~Second order~")
print(*runge_kutt_2_sys([1, 2], 1, 10, 0, [1.5, 0]), sep='\n')
print()
print("~Fourth order~")
print(*runge_kutt_4_sys([1, 2], 1, 10, 0, [1.5, 0]), sep='\n')


