


l = [100, 200, 300, 400, 5880, 3, 300, 88]

def last_occurance_of_number(index_, list_, target):
    if list_[index_] == target:
        return index_
    else:
        if index_ > 0:
            index_ -= 1
            return last_occurance_of_number(index_,list_, target)
        else:
            return None

print(last_occurance_of_number(index_ = len(l)-1, list_=l, target=300))
