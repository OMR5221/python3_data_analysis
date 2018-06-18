# Issue: Perform aggregate calcs (min(), max(), sorting) on a dictionary of data

prices ={
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB' : 10.75
}

# IN ORDER TO PERFORM CALCS it helps to invert the key and values of the dict using zip()
# so that the function is working on the value rather than the key:
# This also allows us to keep the vales in terms of their keys:
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip creates an iterator which can only be used once
