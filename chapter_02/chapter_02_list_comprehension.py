
sizes = ("XS", "S", "M", "L", "XL")
colors = ("Green", "Black", "White")

if __name__ == "__main__":
    print("Building a cartesian product")

    # you can change color to size and will sort differently the cartesian list
    cartesian = [(color, size) for color in colors for size in sizes]
    cartesian = [(color, size) for color in colors 
                               for size in sizes]

    print(cartesian)