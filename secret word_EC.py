import random

number = random.randint(0,3)

words = ["ELIZABETH","IS","VERY","MAD"]
hint1 = ["yours truly","to be","adjective","angry"]
hint2 = ["me","two letters","exagerating the stregth of a word","upset"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter' for help or 'give up' to kill the game.")
    guess = input()

    if guess == secretword:
        print("You win")
        print("It took you " + str(counter) + " guesses.")

    elif guess == "HINT2":
        print( hint2[number] )

    elif guess ==  "HINT1":
        print( hint1[number] )

    elif guess == "FIRST LETTER":
        print( secretword[0] )

    elif guess == "GIVE UP":
        print("The word was " + secretword)
        break

    else:
        counter += 1
        print("Try Again")
