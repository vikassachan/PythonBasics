#fromkeys

#d = {'name': 'unknown', 'age': 'unknown'}

d = dict.fromkeys(['name','age','height'],'unknown')
print(d)


#get method(useful)

d = {'name':'vikas','age':'unknown'}
#print(d['names'])

print(d.get('names')) # better # output will be none
d1 = d.copy()
d.clear()
print(d)

print(d1)