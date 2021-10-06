#Example

#[1,2,3,4]--- > [4,3,2,1]
#['word1','word2']---> ['word2','word1']

#We can also do this with reverse method or [::-1]

# def reverse_list(m):
#     reverse =m[::-1]
#     print(reverse)


# def reverse_list(l):
#     l.reverse()
#     return l



def reverses_list(j):
    rever = []
    for i in range(len(j)):
        m = j.pop()
        rever.append(m)
    return rever
 


l = [1,2,3,4,5,6]
print(reverses_list(l))