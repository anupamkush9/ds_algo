def activity_selection_problem(l):
    sorted_list = sorted(l, key=lambda x: x[1])
    activity_count = 0
    current_val = 0
    selected_acitivity = []
    for ele in sorted_list:
        if current_val < ele[0]:
            activity_count += 1
            current_val = ele[1]
            selected_acitivity.append(ele)
    return activity_count, selected_acitivity
    
l = [(5,9), (1,2), (3,4), (0,6), (5,7), (8,9)]
activity_count, selected_acitivity = activity_selection_problem(l)
print("activity_count:::",activity_count)
print("selected_acitivity:::",selected_acitivity)


# ref : https://www.tutorialspoint.com/Activity-Selection-Problem