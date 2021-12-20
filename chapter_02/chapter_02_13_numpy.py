import numpy as np
from time import perf_counter as pc

a = np.arange(12)
big_a = np.arange(10_000_000)

if __name__ == "__main__":
    print(a)
    print(a * 2)

    a.shape = 3, 4
    print(a)
    print(a[0, :])
    print(a[:, 1])
    print(a.transpose())

    st = pc()
    big_a = big_a/3
    print(pc()- st)