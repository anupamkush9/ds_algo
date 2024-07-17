def findDuplicateparenthesis(brackets):
    stack = []
    for bracket in brackets:
        if bracket != ")":
            stack.append(bracket)
        elif bracket == ")":
            count = 0
            last_item = stack.pop()
            while '(' != last_item:
                count += 1
            if count < 1:
                return True
    return False
   
brackets = "((a+b)+((c+d)))"
brackets = "(a+b)"
brackets = "((a+b+(c+d)))"
print(findDuplicateparenthesis(brackets))

# question ref : https://www.geeksforgeeks.org/problems/expression-contains-redundant-bracket-or-not/1
# implementation dry and run ref : https://www.prepbytes.com/blog/stacks/expression-contains-redundant-bracket-or-not/