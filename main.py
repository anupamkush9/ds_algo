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
            current_capacity += weight
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