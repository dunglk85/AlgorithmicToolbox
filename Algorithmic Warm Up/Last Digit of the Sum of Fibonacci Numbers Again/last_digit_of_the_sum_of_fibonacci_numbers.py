# python3

def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10

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

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    return (fibonacci_number_again(n+2, 10) + 9) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
