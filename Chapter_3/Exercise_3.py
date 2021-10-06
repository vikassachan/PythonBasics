#While loop exercise

#sum of n natural number

# n= input("Enter a number: ")
# n =int(n)
# total = 0
# i = 1
# while i<=n:
#     total = total+i
#     i+=1
# print(total)


## Exercise
num1= input("Enter a num containing more than one digit: ")
n=len(num1)

total =0
i=0
while i<=n-1: #string index 1 less than lenth
    total = total + int(num1[i])
    i+=1
print(total)
