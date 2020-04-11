#!/usr/bin/env python3

import random
import timeit
from typing import List

def find_cycle_sort(array: List[int]) -> int:
    """
    Sorts the array and does a linear scan to find a duplicate number in a valid input array.
    O(n) space and O(n*log(n)) time complexity.
    """

    sorted_array = sorted(array)

    last_value = None
    for v in sorted_array:
        if v == last_value:
            return v
        last_value = v

    return None

def find_cycle_set(array: List[int]) -> int:
    """
    Notes down every number it has seen using a set. If it sees a value twice, it has found the duplicate.
    O(n) space and O(n) time complexity.
    """

    seen = set()
    for v in array:
        if v in seen:
            return v
        seen.add(v)
    return None


def find_cycle_floyd(array: List[int]) -> int:
    """
    Implements an O(1) space and O(n) time complexity algorithm for finding a duplicate number.
    Also called Floyd algorithm, shown in this video: https://www.youtube.com/watch?v=pKO9UjSeLew
    """

    start = array[0]

    tortoise = start
    hare = start

    # Let them advance until they meet
    while True:

        # Check that the input actually was valid for this problem
        assert tortoise < len(array)
        assert hare < len(array)

        tortoise = array[tortoise]
        hare = array[array[hare]]  # Hare takes two hops

        if tortoise == hare:
            break

    assert hare == tortoise

    # both met at node hare/tortoise
    # Now put hare back to start and let him run as slow as the tortoise
    # Where they meet is the point of the cycle start
    hare = start
    while hare != tortoise:
        hare = array[hare]
        tortoise = array[tortoise]

    return hare


def generate_problem(n: int, max_duplicate_count: int = 10):
    res = [0] * (n + 1)

    duplicate_number = random.randint(1, n)

    for i in range(1, n + 2):
        if i == n + 1:
            res[i - 1] = duplicate_number
        else:
            res[i - 1] = i

    for i in range(0, random.randint(0, max_duplicate_count)):
        res[i] = duplicate_number

    random.shuffle(res)

    return res


def main():
    # data = [3, 1, 3, 4, 2]
    data = generate_problem(10000000, 1000)

    # c = find_cycle_sort(data)
    # print(f'find_cycle_sort(data): {c}')
    d = timeit.timeit(lambda: find_cycle_sort(data), number=10)
    print(f'find_cycle_sort(data):\t{d}s')

    # c = find_cycle_set(data)
    # print(f'find_cycle_set(data): {c}')
    d = timeit.timeit(lambda: find_cycle_set(data), number=10)
    print(f'find_cycle_set(data):\t{d}s')

    # c = find_cycle_floyd(data)
    # print(f'find_cycle_floyd(data): {c}')
    d = timeit.timeit(lambda: find_cycle_floyd(data), number=10)
    print(f'find_cycle_floyd(data):\t{d}s')

if __name__ == "__main__":
    main()