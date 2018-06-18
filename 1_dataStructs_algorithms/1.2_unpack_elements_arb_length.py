# 1.2: Unpacking Elements from Iterables of Arbitrary Length

# Issue: Need to unpack N elements from an iterable, but the iterable may be longer than N elements
# Essentially we don't want to create many variables for the large number of elements:

# We can use * to group values into a list associated to many elements:

# We can define a method to drop first and last grades and average all others:
import math

def drop_first_last(grades):

    first, *middle, last = grades
    print(middle)
    return sum(middle) / len(middle)



gr = [56, 100, 75, 67, 76, 88, 65, 97, 45]
avg_gr = drop_first_last(gr)
print(avg_gr)

# Another case where user records consist of a name, and email followed by phone numbers:
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# We could use this to check most recent quarter sales to past quarter sales:

quarter_sales = (900, 765, 849, 347, 883, 934, 445, 849, 458)
*past_quarters, current_quarter = quarter_sales
past_avg = sum(past_quarters) / len(past_quarters)
# return avg_comapre(past_avg, current_quarter) # Possibly perform some other visualizations as well


# We can use to perform different functions on various record types:
records =[
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x,y):
    print('foo', str(x), str(y))

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# WE CAN ALSO USER * UNPACKING TO PROCESS strings:
line = 'oramirez:*:-2:2:Unprivileged User:/home/root/:/usr/local/bash'
uname,*fields, accessDir, sh = line.split(':')
print(uname)
print(accessDir)
print(sh)

# We can also use the * unpacking to ignore bulk values:
record = ('ACME', 50, 123.45, (12,18,2012))
name, *_, (*_, year) = record
print(name)
print(year)

# Cann use to split a list:
items = [1,2,3,4,5,6]
head, *tail = items

print(head)
print(tail)

# WE COULD USE FOR RECURSION BUT pYTHON HAS A RECURSIVE LIMIT SO NOT TO GOOD FOR THIS:
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))