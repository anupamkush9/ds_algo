"""
Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
Output: 240.000000
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240


Input: val[] = [500], wt[] = [30], capacity = 10
Output: 166.670000
Explanation: Since the item’s weight exceeds capacity, we take a fraction 10/30 of it, yielding value 166.670000.
"""


def fractional_knapsack(values, weights, capacity):
    ratios = [ values/weight for values,weight in zip(values, weights)]
    
    # for sorting on the basis of ratio. ( zip function will sort on the basis of ratio)
    sorted_ratios = sorted(zip(ratios, values, weights), reverse=True)
    current_capacity = 0
    max_value = 0
    taken_items = []
    
    for ratio, value, weight in sorted_ratios:
        if current_capacity + weight <= capacity:
            current_capacity += weight
            max_value += value
            taken_items.append(1)
        else:
            fraction = (capacity-current_capacity)/weight
            max_value += fraction*value
            current_capacity += fraction * weight
            taken_items.append(fraction)
            break
    return max_value, taken_items            
            
    
# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, fractions = fractional_knapsack(values, weights, capacity)

print("Maximum value:", max_value)
print("Fractions of items taken:", fractions)

# Ref : https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
