# array_of_tuples = [(3, 'c'), (1, 'a'), (2, 'b')]
# sorted_array = sorted(array_of_tuples, key=lambda x: x[1])

# print(sorted_array)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


array_of_tuples = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_array = sorted(array_of_tuples, key=lambda x: x[1], reverse=True)

print(sorted_array)  # Output: [(3, 'c'), (2, 'b'), (1, 'a')]
