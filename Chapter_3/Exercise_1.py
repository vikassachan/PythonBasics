#Exercise, Number Guessing Game
#Make a variable, like winning_number and assign any number to it
#Ask user to guess a number
#if user guessed correctly then print "YOU WIN !!"
#else "too low" or "too high"

Winning_num = "50"
Guess_Num = input("Guess the Num: between 1 to 100 ")
if Guess_Num==Winning_num:
    print("YOU WIN !!!")
elif Guess_Num>=Winning_num:
    print("Too High")
else:
    print("Too Low")    




