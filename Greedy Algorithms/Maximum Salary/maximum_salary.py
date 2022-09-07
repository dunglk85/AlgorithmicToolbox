# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def is_greater(a,b):
    return int(a + b) >= int(b + a)

def largest_number(numbers):
    numbers = list(map(str, numbers))
    answer = []
    count = len(numbers)
    while count>0:
        max_number = ""
        for number in numbers:
            if is_greater(number, max_number):
                max_number = number
        answer.append(max_number)
        numbers.remove(max_number)
        count -= 1
    return int("".join(answer))



if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
