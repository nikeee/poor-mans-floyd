# Poor Man's Floyd

Floyd's algorithm implemented for an array as well as a directed graph where every node has a maximum of one successor (or simple: a linked list that might have a cycle).

Seen in this video: https://www.youtube.com/watch?v=pKO9UjSeLew

While I was browsing GitHub, I found [this repository](https://github.com/maciej-nowak/ITS-Floyd-Cycle-Detection). It uses floyd's cycle detection to find hash collisions. It might be interesting as further reading and practical application of this algorithm.

## Benchmarking Result

### Memory Usage
```shell
$ pipenv install
$ pipenv shell

$ python3 -m memory_profiler profile.py
```

Results on my machine (Windows 10, running python3 in legacy WSL, i5-3570, 16GB RAM)
```
Filename: profile.py

Line #    Mem usage    Increment   Line Contents
================================================
     9    400.0 MiB    400.0 MiB   @profile
    10                             def main():
    11    401.2 MiB      1.2 MiB       find_cycle_sort(data)
    12    402.6 MiB      1.4 MiB       find_cycle_set(data)
    13    402.6 MiB      0.0 MiB       find_cycle_floyd(data)
```

### Wallclock Time
```shell
$ python3 main_array.py
```
Results on my machine (same setup as above):
```
find_cycle_sort(data):  95.93714189999992s
find_cycle_set(data):   0.2260710000000472s
find_cycle_floyd(data): 0.7033440999998675s
```

### Conclusion
Although `find_cycle_set` and `find_cycle_floyd` have the same time complexity on paper, it depends on the input. floyd genereally seemed a bit slower than the naive `set` implementation. On large inputs however, floyd used a lot less memory compared to the other two methods.
Floyd uses only two pointers whereas the set implementation uses a set (of size up to `n`) and the sort implementation an array (of size exactly `n`).

Take this with a grain of salt as the profiling was done without deep knowledge on how to measure these things properly. Also, it was done inside Legacy WSL which leads to pretty poor performance in general.
