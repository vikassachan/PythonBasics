user = {}

name= input('name:')
age = input('age:')
fav_mov = input('fav mov:').split(',')

user['name'] = name
user['age'] = age
user['fav_mov'] = fav_mov

print(user)

for key, value in user.items():
    print(f"{key}:{value}")