#list comprehension
#with the help of list comprehention we can create list in one line

#create a list of squares from 1 to 10

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)  

#using lc

square2 = [i**2 for i in range(1,11)]
print(square2)

#print 1 to 10 negetive numbers
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

nw_negative = [-i for i in range(1,11)]
print(nw_negative)

#Next Problem

names = ['Vikas', 'Mohit', 'Rohit']
#new_list = ['H','M','R']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

new_list2 = [name[0] for name in names]
print(new_list2)





