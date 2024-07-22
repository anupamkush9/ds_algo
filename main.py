# L = [ {‘x’: 3}, {‘x’: 1}, {‘x’: 2} ]
# Sort it based on x value in ascending order. 
# Expected output: [ {‘x’: 1}, {‘x’: 2}, {‘x’: 3} ]

L = [ {'x': 3}, {'x': 1}, {'x': 2} ]
sorted_L = sorted(L, key=lambda k: k['x'])
print(sorted_L)