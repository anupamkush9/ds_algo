"""
 Input:
 [
     ("sam", 10), ("Amit", 30), ("samar", 50),
     ("sam", 70), ("samar", 20), ("sam", 90),
     ("Ankit", 50), ("sam", 30), ("Amit", 50),
     ("Ankit", 10)
 ]

 Output:
 {
     'sam': 200,
     'Amit': 80,
     'samar': 70,
     'Ankit': 60
 }
 
"""

def sum_by_name(data):
    result = {}
    for name, amount in data:
        result[name] = result.get(name, 0) + amount
    return result

# Example
input_data = [
    ("sam", 10), ("Amit", 30), ("samar", 50), ("sam", 70),
    ("samar", 20), ("sam", 90), ("Ankit", 50), ("sam", 30),
    ("Amit", 50), ("Ankit", 10)
]

output = sum_by_name(input_data)
print(output)