from time import time
import numpy as np
from functools import cache


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@cache
def tribonacci(n):
    # base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    # recursive case
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def count_permutations(lst):
    d = np.diff(lst)
    result = 1
    ones_count = 0
    for i in d:
        if i == 1:
            ones_count += 1
        else:
            if ones_count in [0, 1]:
                ones_count = 0
            else:
                result *= tribonacci(ones_count)
                ones_count = 0
    if ones_count > 1:
        result *= tribonacci(ones_count)
    return result


# Example usage:
# l = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
# print(count_permutations(l))  # Output 8
# l = [0, 1, 2, 3, 4]
# print(count_permutations(l))  # Output 7
# l = [0, 1, 2, 3, 4, 5]
# print(count_permutations(l))  # Output 13
# l = [0, 3, 4, 5]
# print(count_permutations(l))  # Output 2
# l = [0, 3, 4, 5, 6, 9]
# print(count_permutations(l))  # Output 4


@timer_func
def day10(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    adapters = [int(x) for x in lines]
    adapters.append(max(adapters) + 3)
    adapters.append(0)
    adapters.sort()
    difference = np.diff(adapters)

    if not part2:
        return np.count_nonzero(difference == 1) * np.count_nonzero(difference == 3)
    else:
        c = count_permutations(adapters)
        return c


def main():
    assert day10('test10_1') == 7 * 5
    assert day10('test10') == 220
    print(f"Part 1: {day10('input10')}")

    assert day10('test10_1', True) == 8
    assert day10('test10', True) == 19208
    print(f"Part 2: {day10('input10', True)}")


if __name__ == '__main__':
    main()
