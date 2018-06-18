# Generators: a type of function that lazily "returns" results, pausing after each one untilther next is requested.
#  we can iterate over an otherwise infinite loop in this manner:
# It "saves" its progress rather than completely terminating all instances of the function upon yielding.
# Must use yield to be a generator
# Generators: generating a series of values

# Allows us to perfrom as many operations as necessary until we are satisfied with results
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))

    for i in range(1, n+1):
        yield i ** 2



my_squares = squares(1000)

for i in my_squares:
    if i > 1000:
        break
    else:
        print(i, end=' ')

print()

# Generator Expressions: Use inline/more concise manner to make a generator:
# Yield does not need to be explicitly defined
gen = (x ** 2 for x in range(1000))

# print(gen)

print('SUM: ' + str(sum(x **2 for x in range(100))))
print('MIN: ' + str(min(x **2 for x in range(100))))
print('MAX: ' + str(max(x **2 for x in range(100))))

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x # Is a type of return statement that returns results as the code runs
        x += increment

# We can iterate over using a for loop or a function that uses an iterable:
for n in frange(0,4,0.5):
    print(n)


frange_list = list(frange(0,1,0.125))

print(frange_list)


# write a function that takes aN INT AND returns ALL numbers afterward which are prime numbers:

# Normal method would require us to try to generate a list to keep results
# which for a possible infinite result would use up all system memory:
import math

# Non generator verison would continue looping infinitely before crashing:
def get_primes_nong(start):
    result_list = list()
    for element in range(start):
        if is_prime(element):
            result_list.append()

    return result_list

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

# Generator version: yields results one at a time to another iterator
def get_primes(start):
    while True:
        if is_prime(start):
            yield start
        start += 1



# THIS IS THE FUNCTION WE USE TO CALL THE GENERATOR:
def solve_number_10():
    total = 2

    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

sum_primes = solve_number_10()
print(sum_primes)


# wE CAN ALSO RETURN VALUES from the calling function to the generator:
def get_primes_2(number):
    while True:
        if is_prime(number):
            # we can set number to a different value each time the generator yields
            number = yield number
        number += 1


def print_successive_primes(iterations, base=10):
    prime_generator = get_primes_2(base)
    prime_generator.send(None)
    for power in range(iterations):
        # Passing back new value to generator
        print(prime_generator.send(base ** power))

print_successive_primes(10,10)
