#Example
# ['abc','tuv','xyz']---> ['cba','vut','zyx']


def rev_ele(l):
    revele=[]
    for i in l:
        ko = i[::-1]
        revele.append(ko)
    return revele    
    
ls = ['abc','tuv','xyz']
print(rev_ele(ls))

    
