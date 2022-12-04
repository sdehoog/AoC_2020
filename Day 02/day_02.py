def day02(filepath, positions=False):
    with open(filepath) as fin:
        pwds = fin.readlines()

    pwds = [line.split() for line in pwds]
    pwds = [{'minL': int(a.split('-')[0]),
             'maxL': int(a.split('-')[1]),
             'reqL': b[0],
             'password': c}
            for a, b, c in pwds]
    good_count = 0
    if not positions:
        for password in pwds:
            if password['reqL'] in password['password']:
                letter_count = password['password'].count(password['reqL'])
                if password['minL'] <= letter_count <= password['maxL']:
                    good_count += 1
    else:
        for password in pwds:
            if (password['password'][password['minL'] - 1] == password['reqL']) != (password['password'][password['maxL'] - 1] == password['reqL']):
                good_count += 1

    return good_count


def main():
    assert day02('test02') == 2
    print(day02('input02'))

    assert day02('test02', True) == 1
    print(day02('input02', True))


if __name__ == '__main__':
    main()
