# return vs print

#1

def add_three(a,b,c):
    print(a+b+c)

add_three(1,2,3)

#Function practice

#2
def last_char(name):
    return name[-1]
    
print(last_char("Vikas"))

#3
def odd_even(num):
    if num%2 ==0:
        return "Even"
    return "Odd"

print(odd_even(int(input("Enter number:"))))        

#4
def is_even(num):
    if num%2 == 0:
        return True
    return False    

print(is_even(int(input("Enter number:"))))


#5
def is_even(num):
    return num%2 ==0 #true

print(is_even(10) ) 


def song():
    return "Happy Birthday"
print(song())