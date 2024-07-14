def remove_duplicate(s, index):
    if index == len(s)-1:
        return s[index]
    if s[index] not in s[index+1:]: 
        return s[index] + remove_duplicate(s, index +1)
    return remove_duplicate(s, index +1)

print(remove_duplicate("anupam", 0))