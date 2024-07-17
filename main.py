def areBracketsBalanced(brackets):
    stack = []
    bracket_pairs = {'[':']','(':')','{':'}'}
    
    for bracket in brackets:
        if bracket in bracket_pairs.keys():
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            elif bracket_pairs.get(stack.pop()) != bracket:
                return False
    return len(stack) == 0

   
brackets = "[()]{}}{[()()]()}"
# brackets = "[(])"
print(areBracketsBalanced(brackets))

# ref : https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/