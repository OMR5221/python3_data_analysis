# Keep a dictionary ordered

# Can use an OrderedDict:
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])


# Best used to precisely control the order of fields appearing in a JSON encoding:
import json
json.dumps(d)
