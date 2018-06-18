# Issue: Want to make a list of the largest and smallest N items in a collection

# heapq: has 2 functions
# 1. nlargest()
# 2. nsmallest()

# Heap: orders elemtns of a list
# Good for instances in which we want only a few of a large N number of elements
# USE MIN OR MAX() IF YOU JUST NEED ONE Value
# uSE A SPLIT/SLICE IF YOU need a larger collection of the values in N: sorted(items)[:N]
import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]

print(heapq.nlargest(3, nums))

print(heapq.nsmallest(3, nums))

# Can be used with a more complex data structure:
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.3},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


cheapest_stocks = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheapest_stocks)
expensive_stocks = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive_stocks)

# Orders list: The heap[0] element is always the smallest
heap = list(nums)
heapq.heapify(heap)
print(heap)

# pop the element in 0 index
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))