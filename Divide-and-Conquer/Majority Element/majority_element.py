# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0
def majority_element_rec(elements, lo, hi):
    if lo == hi:
        return elements[lo]
    else:
        mid = (lo+hi)//2
        left = majority_element_rec(elements, lo, mid)
        right = majority_element_rec(elements, mid+1, hi)
        if left == right:
            return left
        left_count = sum(1 for i in range(lo, hi+1) if elements[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if elements[i] == right)
        return left if left_count > right_count else right
def majority_element(elements):
    assert len(elements) <= 10 ** 5
    lo = 0
    hi = len(elements) - 1
    el = majority_element_rec(elements, lo, hi)
    return 1 if 2*elements.count(el) > hi+1 else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
