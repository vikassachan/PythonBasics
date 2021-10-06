#filter odd even
#define a function

#input

#list --->[1,2,3,4,5,6,7]
#Output ---> [[1,3,5,7], [2,4,6]]

def odd_even(l):
    filtero = []
    filtere =[]
    filteroe = []
    
    for i in l:
        if i%2 != 0:
            oo=filtero.append(i)
        else:
           ee= filtere.append(i)
    output = [filtero,filtere]           
    return output

lt  = [1,2,3,4,5,6,7] 
print(odd_even(lt))


