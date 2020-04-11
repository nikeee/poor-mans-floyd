#!/usr/bin/env python3

from memory_profiler import profile
from main_array import *


data = generate_problem(10000000, 1000)

@profile
def main():
    find_cycle_sort(data)
    find_cycle_set(data)
    find_cycle_floyd(data)

if __name__ == "__main__":
    main()
