# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    sum = 0
    i = 0
    while sum != n:
        i += 1
        if sum + i <= n:
            summands.append(i)
            sum += i
        else:
            i -= 1
            sum -= summands[-1]
            summands.remove(summands[-1])


    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
