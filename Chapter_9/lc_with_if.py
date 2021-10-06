#list comprehension with if statement
#[1,2,3,4,5,6,7,8,9,10]
#even_nums = [2,4,6]


numbers = list(range(1,11))

nums = []

for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)        

#Even_nums
even_nums = [i for i in numbers if i%2 ==0]
print(even_nums)

#Odd_Nums
odd_nums = [i for i in numbers if i%2 !=0]
print(odd_nums)


