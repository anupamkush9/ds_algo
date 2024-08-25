def change_array(index, l, val):
    if index == len(l):
        print("change_array :: ",l)
        return
    l[index] = val
    change_array(index+1, l, val+1)
    l[index] = l[index] - 2

l = [1,2,3,4,5]
change_array(0, l, 1)
print("main:::",l)
