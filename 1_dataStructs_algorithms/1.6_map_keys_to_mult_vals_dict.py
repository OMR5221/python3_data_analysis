# Create a dictionary that maps keys to mre than 1 value: multidict

"""
Normal dictionary maps each key to a single value:

# keeps insertion order
d =
{
    'a' : [1,2,3],
    'b' : [4, 5]
}

# Sets:  eliminate dupes
e =
{
    'a' : {1,2,3},
    'b' : {4,5}
}

"""

# defaultdict: automatically initializes the first value:
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# If ypu want the same for a regular dict the you need to use the setdefault()
d = {} # regular dict
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

# tHE NORMAL WAY i HAVE DONE THIS IS AS
d = {}
pairs = [('a', 1), ('a', 2), ('b', 4)]

for key, value in pairs:
    if key not in d:
        d[key] = []

    d[key].append(value)
