#kwargs (keyword argument)
# ** kwargs (double star operator)

#output as a dictionary

#kwargs as a parameter

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")

#dictionary unpacking
d = {'name':'Harshit', 'age':24 }
func(first_name = 'Vikas',last_name = 'sachan')  
func(**d)


