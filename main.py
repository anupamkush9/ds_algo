# Naive Approach — Using a Temporary Stack
def insert_at_bottom(stack, item):
    temp = []

    # Step 1: Pop all elements into temp stack
    while stack:
        temp.append(stack.pop())

    # Step 2: Push the new element at the bottom
    stack.append(item)

    # Step 3: Push everything back
    while temp:
        stack.append(temp.pop())

    return stack

# # Example
# stack = [1, 2, 3, 4]   # 4 is top
# insert_at_bottom(stack, 0)
# print(stack)  # [0, 1, 2, 3, 4]


# Better Approach — Recursion (no extra stack)
def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
    else:
        top_element = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(top_element)

# Example usage
stack = [1, 2, 3, 4]
element_to_insert = 0

print("Original Stack:", stack)
insert_at_bottom(stack, element_to_insert)
print("Stack after inserting at bottom:", stack)

# https://iq.opengenus.org/insert-element-at-bottom-of-stack/
# https://www.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/0
