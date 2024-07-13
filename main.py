def check_sorted_array(l):
    if len(l) == 1:
        return True
    if l[0] < l[1]:
        return check_sorted_array(l[1:])
    else:
        return False

l = [10, 20, 300, 40, 50]
print(check_sorted_array(l))


