# 1.1 Unpacking a Sequence into Separate Variables:

# We have an N element tuple/sequence to unpack into a collection of N variables:

# Tuple of 2 elements:
p = (4,5)

x, y = p

print(str(x))
print(str(y))

data = ['ACME', 50, 91.1, (2012, 12,12)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

# Will fail if the number of variables != number of elements:

# Works with any iterable object: lists, tuples
# but also strings, files, iterators, and generators
s = 'Hello'
a, b, c, d, e = s

print(a)
print(b)
print(c)
print(d)
print(e)

# We can ignore vals using the _ operator:
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
