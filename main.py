"""
a program for Flattening an array
INPUT:  [1 , 2 , [3, [4,5]]];
OUTPUT:  [1,2,3,4,5]

INPUT:   [[1 , 2], [3 , 4], [5 , 6]];
OUTPUT:  [1,2,3,4,5,6]
"""

result = []

def get_elements(list_):
    for i in list_:
        if type(i) != list:
            result.append(i)
        else:
            get_elements(i)
    return result

list_ = [1, 2, [3, [4, 5]]]

print(get_elements(list_))