# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.
# Example
# capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

def capitalizeFirst(arr):
    result_list = []
    if len(arr)==1:
        result_list.append(arr[0].capitalize())
        return result_list
    else:
        result_list.append(arr[0].capitalize())
        return result_list + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'taco', 'banana']))