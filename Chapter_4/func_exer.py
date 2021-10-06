##Greater
def greater(a,b):
    if a > b:
        return a
    else:
        return b    

# num1 = int(input("Enter ist num:"))
# num2 = int(input("Enter 2nd num:"))
# bigger= greater(num1,num2)
# print("Greater of the two is:"+str(bigger))


##Greatest

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(100,34,76))   

##3
def new_greatest(a,b,c): 
    return greater(greater(a,b),c)
print(new_greatest(100,25,165))    




