Resumen Fluent Python:

****************************CHAPTER 1****************************

1. Chapter 1: The Python Data Model
-> Cards:
--> __getitem__ if implemented add slicing, in/contains and iteration functionality.

-> Vectors:
—-> __repr__ is used for representation/logging (you must be able to replicate the class).
--> __str__ is intended for end user.
--> Reversed operators: are fallbacks used when operands are swapped (b * a instead of a * b).
--> Augmented assignments are shortcuts combining an infix operator with variable assign‐ ment (a = a * b becomes a *= b).

****************************CHAPTER 2****************************

2. Chapter 2: An Array of Sequences.

Container Sequences: list, tuple and collections.deque. Can hold any type of items.
Flat Sequences: can only hold primitive values (but are more compact).

ABC: abstract based classes.

In Python line breaks are ignored in [], {}, ()

ord: converts to unicode integer position
chr: converts from unicode integer position to text

The "key" in sorted should be a function that takes an input and returns a value to be sorted by.

% parameters accepts tuple unpacking when used like this:

    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

Tuple are very handy :)

Multidimensional Slicing and Ellipsis
to evaluate a[i, j], Python calls a.__getitem__((i, j)).
The ellipsis—written with three full stops (...) and not ... (Unicode U+2026)—is rec‐ ognized as a token by the Python parser. It is an alias to the Ellipsis object, the single instance of the ellipsis class.2 As such, it can be passed as an argument to functions and as part of a slice specification, as in f(a, ..., z) or a[i:...]. NumPy uses ... as a shortcut when slicing arrays of many dimensions; for example, if x is a four- dimensional array, x[i, ...] is a shortcut for x[i, :, :, :,]. See the Tentative NumPy Tutorial to learn more about this.

 += work is __iadd__ (for “in-place addition”)

l1 *= 2 keeps the same id
L2 = l2 * 2 modifiers the object underneath

Lessons from strange tuple assignment
• Putting mutable items in tuples is not a good idea.
• Augmented assignment is not an atomic operation—we just saw it throwing an exception after doing part of its job.

In Python the convention is: if you modify something in place, you have to return None to "signal" that it changed the object inplace.

20/12/2021.
Bisect is very useful to perform searching of sorted sequences.
You can use bisect_left or bisect_right.

bisect.insort() allows to insert new elements into the sequence so that it will
remain sorted.

Arrays are very convenient because they are really fast.

Numpy and Scipy are also very cool libraries.

Deques are thread safe for multithreading applications. You can use LIFO or FIFO methods to insert at the begging or the end of the deque.

****************************CHAPTER 3****************************
Python sets and dicts are optimized with hash tables.

Keys in dicts must be hashable.

The atomic immutable types (str, bytes, numeric types) are all hashable. A frozen set is always hashable, because its elements must be hashable by definition. A tuple is hashable only if all its items are hashable.

dict.setdefault is more efficient:

In other words, the end result of this line...
my_dict.setdefault(key, []).append(new_value) 
...is the same as running...
if key not in my_dict: my_dict[key] = []
my_dict[key].append(new_value)


# EFFICIENT DICT
index = {}

index_efficient = {}

# this doesn't work, needs a callable
# index_default_dict = collections.defaultdict([])
index_default_dict = collections.defaultdict(list)

occurences = index.get(word, []) # first check: see if you have a word otherwise[] 
occurences.append(location) # append to [] new location
index[word] = occurences # another lookup to add key and values

index_efficient.setdefault(word, []).append(location)

index_default_dict[word].append(location)

NEXT --> The __missing__ Method