import random
randnumber = random.randint(1,100)
# print(randnumber)

userGuess = ""
guesses = 0
out_of_guesses = False
guess_limit = 10
while (userGuess != randnumber) and not(out_of_guesses):
    if guesses < guess_limit:
        userGuess = int(input("Enter your Guess: "))
        guesses +=1
        if userGuess > randnumber:
             print("You! guessed it wrong. Guess a smaller\n")
        elif userGuess < randnumber:
             print("You! guessed it wrong.Guess a larger\n")
    else:
        out_of_guesses = True
    
if out_of_guesses: 
    print("You are out of guesses") 
    
else:
    print(f"You guessed it right in {guesses} attempt")