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


def seat_decode(seat: str) -> int:
    rows = [0, 127]
    for c in seat[:7]:
        half = (rows[1] - rows[0]) // 2
        if c == 'F':
            rows[1] = rows[0] + half
        elif c == 'B':
            rows[0] = rows[1] - half
    if seat[7] == 'F':
        row = rows[0]
    else:
        row = rows[1]

    cols = [0, 7]
    for c in seat[7:-1]:
        half = (cols[1] - cols[0]) // 2
        if c == 'L':
            cols[1] = cols[0] + half
        elif c == 'R':
            cols[0] = cols[1] - half
    if seat[-1] == 'L':
        col = cols[0]
    else:
        col = cols[1]

    return row * 8 + col

@timer_func
def day05(filepath, part2=False):
    with open(filepath) as fin:
        lines = fin.readlines()

    seat_ids = [seat_decode(line.strip()) for line in lines]
    if not part2:
        return max(seat_ids)
    else:
        seat_ids.sort()
        for a, b in zip(seat_ids, seat_ids[1:]):
            if b - a == 2:
                return b - 1


def main():
    assert day05('test05') == 820
    print(f"Part 1: {day05('input05')}")

    # assert day05('test05', True) == 1
    print(f"Part 2: {day05('input05', True)}")


if __name__ == '__main__':
    main()
