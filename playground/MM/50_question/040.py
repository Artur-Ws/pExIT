def fibonacci_series_1(n):

    fib_list = [0, 1]

    for _ in range(0, n - 1):
        fib_list.append(fib_list[-2] + fib_list[-1])

    return fib_list[n]


def fibonacci_series_2(n):
    if n <= 1:
        return n
    return fibonacci_series_2(n - 1) + fibonacci_series_2(n - 2)

def fibonacci_series_3(n):
    p, d = 0, 1
    for _ in range(n):
        p, d = d, p + d
    return p


print(fibonacci_series_1(7))
print(fibonacci_series_2(8))
print(fibonacci_series_3(9))
