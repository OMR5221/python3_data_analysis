# Implement a queue that sorts items by a given priority and always
# returns the item with the highest priority on each pop operation:

# Uses a heapq to implement:
import heapq

class PriorityQueue:

    def __init__(self):
        # instance variables:
        self._queue = []
        self._index = 0 # Defines the priority of the item for duplicate items

    def push(self, item, priority):
        # Use a negative priority to get the largest element first:
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

for item in q._queue:
    print(item)

q.pop()


for item in q._queue:
    print(item)

q.pop()

for item in q._queue:
    print(item)


q.pop()

for item in q._queue:
    print(item)


q.pop()

for item in q._queue:
    print(item)
