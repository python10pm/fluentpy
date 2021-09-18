class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__ should be unambiguous and match the code necesarry
    # to create the instance
    # __str__ is intented for humans
    def __repr__(self) -> str:
        # how to do this in f"" strings??
        return "Vector (%r, %r)" % (self.x, self.y)
        # return f"Vector (!r{self.x}, !r{self.y})"

    def __abs__(self):
        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def __bool__(self):
        return bool(abs(self))

    # define the addition operation
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    # define the multiplication operation
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    v = Vector(x = 3, y = 4)
    vstr = Vector(x = "3", y = "4")
    print(abs(v))
    print(v)
    # print(vstr)
    print(bool(v))
    print(v * 3)