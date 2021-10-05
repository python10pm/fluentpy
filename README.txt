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


