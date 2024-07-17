def revers_str_by_using_stack(s):
    stack = []
    temp = ''
    for element in s:
        stack.append(element)
    stack_len = len(stack)
    for element in range(stack_len):
        temp += stack.pop()
    return temp

s = "anupam"
print("s:::",s)
reverse_str = revers_str_by_using_stack(s)
print("reverse_str",reverse_str)