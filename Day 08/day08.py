from time import time
import copy


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
def day08(filepath, part2=False):
    with open(filepath) as fin:
        lines = fin.readlines()
    ins = []
    for line in lines:
        x, y = line.split()
        ins.append([x, int(y), 0])
    acc = 0
    ins_line = 0
    max_ins_line = len(ins)
    if not part2:
        while ins_line < max_ins_line:
            opp, arg, run = ins[ins_line]
            if run == 1:
                return acc
            if opp == 'nop':
                ins[ins_line][2] = 1
                ins_line += 1
            elif opp == 'acc':
                ins[ins_line][2] = 1
                acc += arg
                ins_line += 1
            elif opp == 'jmp':
                ins[ins_line][2] = 1
                ins_line += arg

    for i in range(len(ins)):
        c_ins = copy.deepcopy(ins)
        if c_ins[i][0] == 'nop':
            c_ins[i][0] = 'jmp'
        elif c_ins[i][0] == 'jmp':
            c_ins[i][0] = 'nop'
        else:
            continue
        acc = 0
        ins_line = 0
        while ins_line < max_ins_line:
            opp, arg, run = c_ins[ins_line]
            if run == 1:
                break
            if opp == 'nop':
                c_ins[ins_line][2] = 1
                ins_line += 1
            elif opp == 'acc':
                c_ins[ins_line][2] = 1
                acc += arg
                ins_line += 1
            elif opp == 'jmp':
                c_ins[ins_line][2] = 1
                ins_line += arg
        else:
            return acc


def main():
    assert day08('test08') == 5
    print(f"Part 1: {day08('input08')}")

    assert day08('test08', True) == 8
    print(f"Part 2: {day08('input08', True)}")


if __name__ == '__main__':
    main()
