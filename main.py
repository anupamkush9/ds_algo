def pairs_in_array(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append(str(f'{arr[i]}{arr[j]}'))
    print(pairs)
arr = [0, 5, 12, 8]
pairs_in_array(arr)
