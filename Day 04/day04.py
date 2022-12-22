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


def passport_checker(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for entry in required:
        if entry not in passport:
            return False
    try:
        if not (1920 <= int(passport['byr']) <= 2002):
            return False
        if not (2010 <= int(passport['iyr']) <= 2020):
            return False
        if not (2020 <= int(passport['eyr']) <= 2030):
            return False
        if not (re.fullmatch(r'(1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in)', passport['hgt'])):
            return False
        if not (re.fullmatch(r'(#[0-9a-f]{6})', passport['hcl'])):
            return False
        if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            return False
        if not re.fullmatch(r'([0-9]{9})', passport['pid']):
            return False
    except ValueError:
        return False
    return True


@timer_func
def day04(filepath, part2=False):
    with open(filepath) as fin:
        passports = fin.read().split('\n\n')

    passports_parsed = []
    for passport in passports:
        passports_parsed.append({})
        for line in passport.split('\n'):
            for entry in line.split():
                field, value = entry.split(':')
                passports_parsed[-1][field] = value

    if not part2:
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        nonvalid = 0
        for passport in passports_parsed:
            for entry in required:
                if entry not in passport:
                    nonvalid += 1
                    break

        return len(passports_parsed) - nonvalid

    valid = 0
    for passport in passports_parsed:
        if passport_checker(passport):
            valid += 1
    return valid


def main():
    assert day04('test04') == 2
    print(f"Part 1: {day04('input04')}")

    assert day04('test04_02', True) == 4
    print(f"Part 2: {day04('input04', True)}")


if __name__ == '__main__':
    main()
