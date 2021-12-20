import array

numbers = array.array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
memv_oct = memv.cast("B")

if __name__ == "__main__":
    print("__main__")
    print(memv)
    print(len(memv))
    print(memv[2])
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)