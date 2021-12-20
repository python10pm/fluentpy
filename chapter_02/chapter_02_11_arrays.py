import array
import random

if __name__ == "__main__":
    floats = array.array("d", (random.random() for _ in range(10 ** 5)))
    # print(floats[-1])

    # fp = open("floats.bin", "wb")
    # floats.tofile(fp)
    # fp.close()

    with open("floats.bin", "wb") as fp:
        floats.tofile(fp)

    with open("floats.bin", "rb") as fp:
        # this won't work
        # floats2 = array.array("d").fromfile(fp, 10 ** 5)
        floats2 = array.array("d")
        floats2.fromfile(fp, 10 ** 5)
    
    print(floats == floats2)
    print("End")