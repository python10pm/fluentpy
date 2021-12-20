import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FORMAT = "{0:2d} @ {1:2d}    {2}{0:<2d}"

SIZE = 7
random.seed(175)
my_list = []

def demo_bisect(bisect_func, needles, haystack):
    for needle in reversed(needles):
        position = bisect_func(haystack, needle)
        offset = position * "  |"
        print(ROW_FORMAT.format(needle, position, offset))

def grade(score, break_points = [60, 70, 80, 90], grades = "FDCBA"):
    position = bisect.bisect_right(break_points, score)
    return grades[position]

if __name__ == "__main__":
    if sys.argv[-1] == "left":
        bisect_func = bisect.bisect_left
    else:
        bisect_func = bisect.bisect_right
    print(f"Demo {bisect_func.__name__}")
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo_bisect(bisect_func = bisect_func, needles = NEEDLES, haystack = HAYSTACK)
    demo_bisect(bisect_func = bisect.bisect_left, needles = NEEDLES, haystack = HAYSTACK)

    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


    print("Using bisect.insort() for insert elements into a ordered sequence.")

    for i in range(SIZE):
        new_item_to_insert = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item_to_insert)
        print("{0:2d} -> {1}".format(new_item_to_insert, my_list))