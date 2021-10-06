#more about get, two same keys i dictionary

user = { 'name' : 'Vikas', 'age' : 26}

print(user.get('name'))
print(user.get('names'))
print(user.get('names', 'Not found'))


