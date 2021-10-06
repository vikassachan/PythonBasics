total   =0
num =input("Enter a number with more than one digit : ")


for i in range(0,len(num)):
    total+=int(num[i])

print(total)
