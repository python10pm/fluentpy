VERBOSE = False

import re
import collections

WORD_RE = re.compile('\w+')

zen_of_python = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

with open("zen_of_python.txt", "w") as f:
    f.write(zen_of_python)

index = {}

index_efficient = {}

# this doesn't work, needs a callable
# index_default_dict = collections.defaultdict([])
index_default_dict = collections.defaultdict(list)

if __name__ == "__main__":

    with open("zen_of_python.txt", "r") as f:
        contents = f.read()

    for line_nr, line in enumerate(contents.split("\n")):
        for match in WORD_RE.finditer(line): # finds any words
            word = match.group()
            column_nr = match.start() + 1
            location = (line_nr, column_nr)
            
            # bad implementation
            occurences = index.get(word, []) # first check: see if you have a word otherwise[] 
            occurences.append(location) # append to [] new location
            index[word] = occurences # another lookup to add key and values

            index_efficient.setdefault(word, []).append(location)

            index_default_dict[word].append(location)

    if VERBOSE: print(index)
    if VERBOSE: print(index_efficient)
    if VERBOSE: print(index_default_dict)

    print(index == index_efficient == index_default_dict)

    for word in sorted(index, key = str.upper):
        if VERBOSE: print(word)
