# import random
# win_num = random.randint(1,100)

win_num = 43

guess =1
user_n = int(input("Guess the num 1 to 100: \n"))
game_over = False

while not game_over:
    if user_n ==win_num:
        print(f"You Win and You guessed this number in {guess} times")
        game_over = True
    else:
        if user_n < win_num:
            print("too low")
            
        else:
            print("too high")    
        
        #DRY - don't repeat urself
        guess+=1
        user_n = int(input("guess again\n"))
