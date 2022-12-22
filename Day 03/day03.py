from time import time
import numpy as np

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


@timer_func
def day03(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mod = len(lines[0])

    tree_counts = []
    for dx, dy in deltas:
        x = 0
        y = 0
        tree_count = 0
        while y < len(lines) - 1:
            x += dx
            x %= mod
            y += dy
            if lines[y][x] == '#':
                tree_count += 1

        tree_counts.append(tree_count)
    if part2:
        result = 1
        for tree_count in tree_counts:
            result *= tree_count
        return result
    else:
        return tree_counts[1]


def main():
    assert day03('test03') == 7
    print(f"Part 1: {day03('input03')}")

    assert day03('test03', True) == 336
    print(f"Part 2: {day03('input03', True)}")


if __name__ == '__main__':
    main()
