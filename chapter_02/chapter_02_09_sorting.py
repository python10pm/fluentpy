l = ['grape', 'raspberry', 'apple', 'banana', "watermelon_fruit", "watermelon fruit"]

if __name__ == "__main__":
    print(l)
    print(sorted(l))
    print(sorted(l, key = len, reverse = True))
    print(l.sort(key = str.lower, reverse = False))
    print(l)