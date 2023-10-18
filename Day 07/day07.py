from time import time
import re


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


def contains_gold(bag, bag_dict):
    val = bag_dict[bag]
    if not val:
        return False
    else:
        if 'shiny gold bag' in val.keys():
            return True
        else:
            return any([contains_gold(s_bag, bag_dict) for s_bag in val.keys()])


def bag_contains(bag, bag_dict):
    val = bag_dict[bag]
    if not val:
        return 1
    contains = sum([v*bag_contains(b, bag_dict) for b, v in val.items()])
    return contains + 1


@timer_func
def day07(filepath, part2=False):
    with open(filepath) as fin:
        lines = fin.readlines()

    bag_dict = {}
    for line in lines:
        bags = re.findall(r'(\w+ \w+ bag)', line)
        nums = re.findall(r'(\d+)', line)
        if bags[1] == 'no other bag':
            bag_dict[bags[0]] = 0
        else:
            bag_dict[bags[0]] = {b: int(c) for b, c in zip(bags[1:], nums)}

    if not part2:
        return sum([1 if contains_gold(bag, bag_dict) else 0 for bag in bag_dict.keys()])

    total = bag_contains('shiny gold bag', bag_dict)
    return total - 1


def main():
    assert day07('test07') == 4
    print(f"Part 1: {day07('input07')}")

    assert day07('test07', True) == 32
    print(f"Part 2: {day07('input07', True)}")


if __name__ == '__main__':
    main()
