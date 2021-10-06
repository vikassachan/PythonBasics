#Q- What are dictionaries
#A- unordered collections of data in key : value pair

#how to create dictionaries

user = {'name':'Harshit', 'age':24}
print(user)
print(type(user))

#second method

user1 = dict(name ='Harshit1', age = 23)
print(user1)

#we cannot access data from dictionary using indexing

print(user['name'])

#which type of data dictionary can store
#anything

user_info = {
    'name': 'vikas',
    'age': 26,
    'fav_movies': ['abc', 'cgr']
}


print(user_info['fav_movies'])


#how to add data to empty dictionary
user_info2 = {}
user_info2['name']='mohit'

print(user_info2)