d1 = dict(one = 1, two = 2)
d2 = {"one":1, "two":2}
d3 = dict(zip(["one", "two"], [1, 2]))
d4 = dict([("one", 1), ("two", 2)])
d5 = dict({"one":1, "two":2})


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

# dict comprehension

DIALS = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States')
]

country_dial_dict = {country:code for code, country in DIALS if code > 1}

if __name__ == "__main__":
    print(d1 == d2 == d3 == d4 == d5)
    print(country_dial_dict)
    print("India" in country_dial_dict)
    # print(a == b == c == d == e)