user_info = {
    'name': 'vikas',
    'age': 26,
    'fav_movies': ['abc', 'cgr'],
    'fav_songs': ['awake', 'believer']
    }

more_info ={'name':'sachan','state': 'haryana', 'hobbies': ['coding','reading','guitar']}

user_info.update(more_info)

for i in user_info.items():
    print(i)


     