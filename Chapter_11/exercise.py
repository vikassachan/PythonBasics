#define function
#input
#num, iterable(tuple, list) containing numbers as args

#example
#nums = [1,2,3]
#to_power(3,*nums)

#output
#list ---> [1**3, 8, 27]

#if user didn't pass any args the give a user a message 'hey you did't pass'
#args

#else
#return list

# NOTE - Use list comprehension

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass anything"
nums = [1,2,3]
print(to_power(2,*nums))

