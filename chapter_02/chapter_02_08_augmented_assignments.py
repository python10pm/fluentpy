l1 = [1, 2, 3]
l2 = [1, 2, 3]
t1 = (1, 2, 3)

# l1 *= 2 keeps the same id
# L2 = l2 * 2 modifiers the object underneath

t2 = (1, 2, [3, 4])

if __name__ == "__main__":
    print(id(l1))
    l1 *= 2
    print(id(l1))

    print(id(l2))
    l2 = l2 * 2
    print(id(l2))

    print(id(t1))
    t1 *= 2
    print(id(t1))

    print(t2)

    try:
        t2[2] += [30, 40]
    except Exception as e:
        print(e)

    print(t2)

    t2[2].extend([5, 60])
    print(t2)