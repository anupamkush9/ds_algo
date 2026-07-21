"""
Input:  {'a': 1, 'b': 2, 'c': {'d': 1, 'e': 2}}
Output: {'a': 1, 'b': 2, 'd': 1, 'e': 2}

Input:  {'x': 1, 'y': {'z': 2, 'w': {'p': 3, 'q': 4}}}
Output: {'x': 1, 'z': 2, 'p': 3, 'q': 4}

Input:  {'a': 1, 'b': {'a': 99}}
Output: {'a': 99}   # collision: nested 'a' overwrites top-level 'a'

Input:  {'a': {'b': {'c': {'d': 1}}}}
Output: {'d': 1}    # deeply nested, still flattens fully

Input:  {}
Output: {}          # empty dict stays empty

Input:  {'a': 1, 'b': 2}
Output: {'a': 1, 'b': 2}   # no nesting, unchanged
"""

def flatten_dict(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            result.update(flatten_dict(value))  # merge nested dict's keys
        else:
            result[key] = value
    return result

# Example
input_dict = {'a': 1, 'b': 2, 'c': {'d': 1, 'e': 2}}
output = flatten_dict(input_dict)
print(output)
# Output: {'a': 1, 'b': 2, 'd': 1, 'e': 2}