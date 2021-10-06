#function with all parameters

#parameter
#*args
#default parameters
#** kwargs

#PADK

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('vikas', 1,2,3, a=1, b=2)