import array

symbols = '$¢£¥€¤'

sizes = ["S", "M", "L"]
colors = ["Black", "Green", "Red"]

if __name__ == "__main__":
    t = tuple(ord(s) for s in symbols)

    # in case of arrays, it is indifferent to start them 
    # from a list or an array
    a = array.array("I", [ord(s) for s in symbols])
    a2 = array.array("I", (ord(s) for s in symbols))

    print(t)
    print(a)
    print(a2)
    print(a == a2)

    # The generator expression yields items one by one; a list with 
    # all six T-shirt variations is never produced in this example.
    for tshirt in (f"{size} {color}" for size in sizes for color in colors):
        print(tshirt)