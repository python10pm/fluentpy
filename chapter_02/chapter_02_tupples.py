import functools

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) # tupple unpacking

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
traveler_ids2 = [('USA', '31195855', 1), ('BRA', 'CE342567', 3), ('ESP', 'XDA205856', 2)]

dummy_tupple = (20, 3)

def multiply(*args):
    return functools.reduce(lambda a, b: a * b, args)

a, _ = dummy_tupple

# help(sorted)

if __name__ == "__main__":

    # key should be a function to sort the values
    print(sorted(traveler_ids2, key = lambda t: t[2]))

    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    print(_)
    print(multiply(*(2, 3, 4))) # tuple 
    print(multiply(2, 3, 4))
    print(divmod(*dummy_tupple))

    # use of tupple unpacking in 2 ways
    # supply to function *
    # and tupple unpacking the results
    quotient, remainder = divmod(*dummy_tupple) 