#set data type
# unordered collection of unique items
# we can't store list,dictionary

s = {1,2,3,2}
print(s) #Index not possible in sets

#output
#{1, 2, 3}

l = [1,2,3,4,5,5,6,7,7,8]
#remove duplicate
s1 = list(set(l))
s2 = set(s1)
print (s2)

#Output
#[1, 2, 3, 4, 5, 6, 7, 8]

s2.add(9)
s2.remove(1)
s2.discard(10) #NoError even if value not available in set

print(s2)

s2.clear()
print(s2)


