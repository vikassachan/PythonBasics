def no_of_lists(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+= 1
    return count

num = [1,2,3,[1,2,3],[1,2,3,4]] 
print(no_of_lists(num))    