

# In Python 2, x would be available inside the list comprehension.
# In Python 3, this is not the case no more.
x = "My Value "

dummy_list = [x for x in "ABC"]

# In Python 3, iterables in list comprehension have local scope
# But the main object is also available and they don't collide.
dummy_list_2 = [ord(x)for x in x]


symbols = '$¢£¥€¤'

if __name__ == "__main__":
    print("Executing as __main__")

    print("Basic lists")
    print(x)
    print(dummy_list)
    print(x, dummy_list_2)

    print("Map, filter")
    beyond_ascii_lc = [ord(c) for c in symbols if ord(c) > 127]

    # crea una lista despúes de aplicar un filtro a una lista mappeada con ord
    beyond_ascii_mf = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii_lc)
    print(beyond_ascii_mf)
