def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False

print(is_palindrom("Vikas")) 
print(is_palindrom("naman"))
