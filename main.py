def is_possible_pair_exists(arr, target):
  arr.sort()
  left = 0
  right = len(arr) - 1

  while left <= right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
      return True
    elif current_sum < target:
      left += 1
    else:
      right -= 1

  return False

l = [1, 5, 7, -1]
target = 6
print(is_possible_pair_exists(l, target))

# Ref : https://www.geeksforgeeks.org/count-pairs-with-given-sum/
