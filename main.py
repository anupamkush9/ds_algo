def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

def merge(left, right, arr):
    left_len = len(left)
    right_len = len(right)
    i = j = k = 0
    
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < left_len:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < right_len:
        arr[k] = right[j]
        k += 1
        j += 1

l = [10,40,55,0,5]        
merge_sort(l)
print(l)

# ref : https://www.youtube.com/watch?v=nCNfu_zNhyI&t=353s
