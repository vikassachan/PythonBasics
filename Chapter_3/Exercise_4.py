##Ex 1

#name= input("Enter Name: ")
# i=0
# while i<len(name):
#     print(f"{name[i]} : {name.count(name[i])}")
#     i+=1


## Non Repeat

name= input("Enter Name: ")
temp=""
i=0
while i<len(name):
    if name[i] not in temp:
        temp +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
    
   

