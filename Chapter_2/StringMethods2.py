#replace() method
#find() method

# string = "is she is beautiful and she is a good dancer"
# print(string.replace("is","was",1))
# print(string.replace("is","was"))

# print(string.find("is"))
# print(string.find("is",1))

##find the "is" position by skipping the first one

# is_pos1 = string.find("is") #is_pos1 ----> Number
# is_pos2 = string.find("is", is_pos1)
# print(is_pos2)
# is_pos2= string.find("is", is_pos1+1)
# print(is_pos2)


# ##***********Center Method
# name = "Vikas"
# ##**Vikas** , 9

# print(name.center(9,"*"))

# name = input("enter your name: ")
# print(name.center(len(name)+8,"*"))

##**String are immutable

name = "Vikas"

print(name[4])
## name[4] = "T" ---->It can't be done
print(name.replace('s','S'))
print(name) #Immutable