from collections.abc import Mapping

tt = (1, 2, ([3], 4 ))
tl = (1, 2, [3, 4 ])
ft = (1, 2, frozenset([3, 4]))


if __name__ == "__main__":
    # print(__builtins__.__dict__)

    print(isinstance({}, Mapping))

    print(hash(tt))
    print(hash(ft))
    print(hash(tl))
