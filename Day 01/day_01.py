def day01(filepath, three=False):
    with open(filepath) as fin:
        entries = [int(a.strip()) for a in fin.readlines()]
    if not three:
        for entry in entries:
            if (2020 - entry) in entries:
                return entry * (2020 - entry)
    else:
        for entry in entries:
            for entry2 in entries:
                if (2020 - entry - entry2) in entries:
                    return entry * entry2 * (2020 - entry - entry2)


def main():
    assert day01('test01') == 514579
    print(day01('input01'))

    assert day01('test01', True) == 241861950
    print(day01('input01', True))


if __name__ == '__main__':
    main()
