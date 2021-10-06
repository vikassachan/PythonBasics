name = "vikas"
age = "26"

print("Hello: " +name+ "\nYour age is: "+str(age))  #ugly syntax

print("Hello: {} \nYour age is {}".format(name,age))

print(f"Hello: {name} \nYour age is: {age}")

##Example

name = "AgeIs"
age1 = 23
age2 = 25

print(f"{name+str(int(age1)+int(age2))}")