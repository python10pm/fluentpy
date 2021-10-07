Resumen Fluent Python:

1. Chapter 1: The Python Data Model
-> Cards:
--> __getitem__ if implemented add slicing, in/contains and iteration functionality.

-> Vectors:
—-> __repr__ is used for representation/logging (you must be able to replicate the class).
--> __str__ is intended for end user.
--> Reversed operators: are fallbacks used when operands are swapped (b * a instead of a * b).
--> Augmented assignments are shortcuts combining an infix operator with variable assign‐ ment (a = a * b becomes a *= b).

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