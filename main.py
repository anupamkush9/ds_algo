


l = [100, 200, 300, 400, 5880]

def first_occurance_of_number(index_, list_, target):
    if list_[index_] == target:
        return index_
    else:
        if index_ < len(l)-1:
            index_ += 1
            return first_occurance_of_number(index_,list_, target)
        else:
            return None

print(first_occurance_of_number(index_ = 0, list_=l, target=300))
