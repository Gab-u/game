import datetime
import random

def guessGame():
    
    setNumber = random.randint(1,50)
    playAgain = "p"
    print("\nWelcome to the 'Guess the number' game\n")
    while playAgain == "p":
        while True:
            try:
                guess = int(input("Guess a number between 1 - 50:\n"))
            except ValueError:
                print("Invalid choice: Try again:")
            else:
                break
        
        while setNumber != guess:
            if guess > setNumber:
                print("Oops! That's too high. Try again: ")
                guess = int(input())
            else:
                print("Oops! That's too low. Try again: ")
                guess = int(input())
        else:
            print("Congratulations!! You guessed it right.")
            print("Press 'p' to play again.")
        playAgain = input()
    

time = datetime.datetime.now()
print(time)
print("\t\nWelcome to game arcade")
print("Choose game number to play.")
print("\t1. Number guessing game.")
print("\t2. Hangman")
print("\t3. TIC TAC TOE")
#gamenum = int(input("I choose game number: "))

while True:
    try:
        gamenum = int(input("I choose game number: "))
    except ValueError:
        print("Invalid choice. Try again.")
    else:
        break
while gamenum <1:
    print("Invalid choice. Try again.")
    gamenum = int(input("I choose game number: "))
    
while gamenum >3:
    print("Invalid choice. Try again.")
    gamenum = int(input("I choose game number: "))
else:
    if gamenum == 1:
        guessGame()
        
    elif gamenum == 2:
        def hangman():
            pass
    elif gamenum == 3:
        def ttt():
            pass

    
