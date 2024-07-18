# Custom function
def activitySelection(start, end):
    end.sort()
    activity_count = 0
    acitvities = []
    
    acitvities.append(0)
    last_activity_end_time = end[0]
    activity_count = 1
    for i in range(1,len(end)):
        if start[i] > last_activity_end_time:
            acitvities.append(i)
            last_activity_end_time = end[i]
            activity_count += 1
    return activity_count
            

# start = [1, 3, 2, 5]
# end = [2, 4, 3, 6]
start = [2, 1]
end = [2, 2]

print("************")
print(activitySelection(start, end))
print("************")

# Ref : https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1
