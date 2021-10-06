name, age = input("Enter name and age: ").split(",")
# age=int(age)
if (name[0]== ("a" or  "A")) and int(age)>=10:
    print("You are eligible")
else:
    print("Not eligible")    


