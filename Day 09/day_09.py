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

def find_no_pairs(lst, n, first_only=True):
    # Initialize an empty list to store the output
    output = []
    # Loop through the list starting from the nth + 1 element
    for i in range(n, len(lst)):
        # Get the current element
        current = lst[i]
        # Get the previous n elements
        previous = lst[i - n:i]
        # Initialize a flag to indicate if there is a pair
        has_pair = False
        # Loop through the previous n elements
        for j in range(n):
            # Get the complement of the current element
            complement = current - previous[j]
            # Check if the complement is in the previous n elements
            if complement in previous[:j] + previous[j + 1:]:
                # There is a pair, set the flag to True and break the loop
                has_pair = True
                break
        # If there is no pair, add the current element to the output list
        if not has_pair:
            if first_only:
                return current
            output.append(current)
    # Return the output list
    return output

# Example usage:
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 3
# print(find_no_pairs(lst, n))  # Output: [4, 5, 6, 7, 8, 9]


def find_contiguous_set(lst, n):
    # Initialize an empty list to store the output
    output = []
    # Check if the list has at least n elements
    if len(lst) < n:
        return output
    # Get the target sum as the nth element of the list
    target = lst[n - 1]
    # Loop through the list from the beginning to the n - 2 element
    for i in range(n - 1):
        # Initialize a variable to store the current sum
        current_sum = lst[i]
        # Initialize a list to store the current set
        current_set = [lst[i]]
        # Loop through the list from the next element to the n - 1 element
        for j in range(i + 1, n):
            # Add the element to the current sum and the current set
            current_sum += lst[j]
            current_set.append(lst[j])
            # Check if the current sum is equal to the target
            if current_sum == target:
                # Add the current set to the output list
                output.append(current_set)
                # Break the inner loop
                break
            # Check if the current sum is greater than the target
            elif current_sum > target:
                # Break the inner loop
                break
    # Return the output list
    return output

# Example usage:
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 5
# print(find_contiguous_set(lst, n))  # Output: [[2, 3]]


@timer_func
def day09(filepath, part2=False, n=25):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    nums = [int(x) for x in lines]
    invalid_number = find_no_pairs(nums, n, True)
    if not part2:
        return invalid_number
    c_slice = find_contiguous_set(nums, nums.index(invalid_number) + 1)
    return min(c_slice[0]) + max(c_slice[0])


def main():
    assert day09('test09', n=5) == 127
    print(f"Part 1: {day09('input09')}")

    assert day09('test09', True, n=5) == 62
    print(f"Part 2: {day09('input09', True)}")


if __name__ == '__main__':
    main()
