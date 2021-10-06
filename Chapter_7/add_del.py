#how to add data in dictionary
user_info = {
    'name': 'vikas',
    'age': 26,
    'fav_movies': ['abc', 'cgr']
}

user_info['fav_song']= ['aaja'],['jaja']

print(user_info)

#pop method

popped_item = user_info.pop('fav_song')
print(f"poppped item is {popped_item}")
print(user_info)

#poptem method

popped_item = user_info.popitem()
print(f"poppped item is {popped_item}")
print(user_info)