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


metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def pretty_print(lt):

    print("{:15} | {:^9} | {:^9}".format("", "lat.", "long."))
    fmt = "{:15} | {:9.4f} | {:9.4f}"

    for name, cc, pop, (lat, long) in lt:
        if long <= 0:
            print(fmt.format(name, lat, long))

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
    
    pretty_print(metro_areas)