#dictionary comprehension
#square = {1:1, 2:4, 3:9}
square = {num:num**2 for num in range(1,11)}
square1 = {f"Square of {num} is":num**2 for num in range(1,11)}
print(square)
print(square1)

for k,v in square1.items():
    print(f"{k} : {v}")

#vikas
string = "Vikas"
word_count = {char:string.count(char) for char in string}
print(word_count)