#Exercise

#define a function that takes a number(n)
#return a dictionary containing cube of numbers from 1 to n

# example
#cube_finder()
#{1:1,2:8,3:27}

def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        
        cube[i] = i**3
    return cube

print(cube_finder(10))

