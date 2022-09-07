# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def get_period(m):
    a = 0
    b = 1
    for i in range(2, m*m + 1):
        c = (a+b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i-1

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    period = get_period(m)
    n = n % period
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n+1):
        c = b
        b = (a + b) % m
        a = c
    return b


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
