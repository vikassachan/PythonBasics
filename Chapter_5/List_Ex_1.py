numbers = [1,2,3,4]

def sqr_list(l):
    square = []
    for i in l:
        square.append(i*i)
    return square 

print(sqr_list(numbers))       