#Find common elements in two lists

# input---> [1,2,3,8],[1,2,7,6]
# Output ---> [1,2]

def com_fin(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output        

print(com_fin([1,2,3,8],[1,2,7,6]))