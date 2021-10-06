# in keywords and iterations in dictionary


user_info = {
    'name': 'vikas',
    'age': 26,
    'fav_movies': ['abc', 'cgr']
}

#check if key exists in dictionary

#Dictionary   'key' : 'value'

if 'name' in user_info:
    print('present')
else:
    print('no') 

#checkif value exists in dictionary

if 'vikas' in user_info.values():
    print('value present')
else:
    print('no') 

#loops in dictionaries

#key
for i in user_info:
    print(i)

#values
for i in user_info.values():
    print(i)

#OR

for i in user_info:
    print(user_info[i])    

user_info_keys = user_info.keys()
print(user_info_keys)

user_info_values = user_info.values()
print(user_info_values)

#you cannot add, delete data from dict values like list, but you can iterate through dict values


#items method

user_items = user_info.items()
print(user_items)

for i, j in user_info.items():
    print(f"key is {i} and value is {j}")
    
for i in user_info.items():
    print(i)


