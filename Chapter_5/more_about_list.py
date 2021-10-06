#generate lists with range functions
#something more about pop method
#index method
#pass list to a function

numbers = list(range(1,11))
#print(numbers)


# print(numbers.pop())

#numbers.index(1)

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers)) 