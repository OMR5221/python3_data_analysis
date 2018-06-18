# Issue: We went to keep the last few items seen during an iteration

# We can use collections.deque() to keep a limited history: Creates a dynamic queue
# We can match a pattern seq and yield N lines of context

from collections import deque

def search(lines, pattern, history = 5):

    # Retains a specific sized queue so that when we add a new element will pop the first element off:
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            # yield is a keyword that is used like return, except the function will return a generator.
            # a generator is an iterators, a kind of iterable you can only iterate over once.
            # Generators do not store all the values in memory, they generate the values on the fly:
            yield line, previous_lines

        # Start refreshing the cache:
        previous_lines.append(line)

# Use on a file:
if __name__ == '__main__':
    with open('1.3_test_file.txt') as f:
        # Get the
        for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')

            print(line, end='')
            print('-'*20)

# Using deque creates a fixed length queue
# Oldest element is popped off (by default from the front)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)


# We can also not define a max limit
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4) # Add an element to the front of the queue
print(q)

q.pop() # Will remove rightmost element
print(q)

q.popleft() # will remove left most element
print(q)