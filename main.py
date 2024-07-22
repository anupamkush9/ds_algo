def maxConsecutivecharacters(l):
    max_consicutive = 1
    max_occurance_char = l[0]
    current_consicutive = 0
    last_char = l[0]
    for ch in l[1:]:
        if ch == last_char:
            current_consicutive += 1
            if current_consicutive > max_consicutive:
                max_consicutive = max_consicutive + 1
                max_occurance_char = ch
        else:
            current_consicutive = 1
        last_char = ch
    return max_consicutive, max_occurance_char            

    
    

l = [1,2,3,3,2,1,2]
l = "geeeeekkkkkk"
print(maxConsecutivecharacters(l))


# Ref : https://www.geeksforgeeks.org/maximum-consecutive-repeating-character-string/
