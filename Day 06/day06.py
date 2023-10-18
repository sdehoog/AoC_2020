from time import time


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
def day06(filepath, part2=False):
    with open(filepath) as fin:
        groups = fin.read().split('\n\n')

    qs_per_group = []
    if not part2:
        for group in groups:
            qs = set()
            for line in group.split('\n'):
                for c in line:
                    qs.add(c)
            qs_per_group.append(len(qs))

    else:
        for group in groups:
            lines = group.split('\n')
            if len(lines) == 1:
                qs_per_group.append(len(lines[0]))
            else:
                group_sets = []
                for line in lines:
                    group_sets.append(set([*line]))
                unique = len(group_sets[0].intersection(*group_sets[1:]))
                qs_per_group.append(unique)

    return sum(qs_per_group)

def main():
    assert day06('test06') == 11
    print(f"Part 1: {day06('input06')}")

    assert day06('test06', True) == 6
    print(f"Part 2: {day06('input06', True)}")


if __name__ == '__main__':
    main()
