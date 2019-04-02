secret_word = "Canada"; #The user needs to put in this word to win
guess = ""
guess_count = 0; #guess count from 0
guess_limit = 5
out_of_guess = False

while guess != secret_word and not(out_of_guess): # user input do not match the secret word and not out of guesses
    if guess_count < guess_limit:
        print("Hint: It is a country famous for the maple leaf!")
        guess = input("Enter your word: "); #user input to guess the word.
        guess_count +=1
    else:
        out_of_guess = True; #user is out of guess

if out_of_guess:
    print ("You lost! Please try again!")
else:
    print("You win!")