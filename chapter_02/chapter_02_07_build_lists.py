# creates a 3 lists that point to the same inner list
wrong_list = [["_"] * 3] * 3
wrong_list[1][2] = "X"

# the above code behaves like this
'''

row = ['_'] * 3 
board = []

for i in range(3):
    board.append(row)
'''

right_list = [["_"] * 3 for _ in range(3)]
right_list[1][2] = "X"

right_list_2 = [["_" for _ in range(3)] for _ in range(3)]
right_list_2[1][2] = "X"

if __name__ == "__main__":
    print(wrong_list)
    print(right_list)
    print(right_list_2)