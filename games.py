

import datetime
import random
import string

list = ["client","leader","location","law","organization","tooth","solution","player","artisan","improvement","platform","customer","quantty","chest","outcome","conclusion","injury","investment","category","judgment","director","goal","cigarette","mom","history","woman","disk","courage","data","department","cousin","thing","memory","speech","library","disaster","engineering","measurement","volume","photo","ladder","payment","movie","efficiency","extent","painting","imagination","hall","grandmother","language"]

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
    

def validWord(list):
    word = random.choice(list)
    while "-" in word or " " in word:
        word = random.choice(list)
         
    return word.upper()

def hangman():
    word = validWord(list)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6
    
    print("\nWelcome to the 'Hangman' game\n")
        
    while len(wordLetters)>0 and lives>0:
        
        print("You have",lives,"lives left and You have used these letters: "," ".join(usedLetters))
        
        print(wordLetters)
        wordVisibility = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: "," ".join(wordVisibility))
        
        userLetters = input("Enter a letter: ").upper()
        if userLetters in alphabet - usedLetters:
            usedLetters.add(userLetters)
            if userLetters in wordLetters:
                wordLetters.remove(userLetters)
            else:
                
                lives = lives - 1
                print("\nNot in the word. Try again")
        elif userLetters in usedLetters:
            print("You have used this letter. Try again: ")
        else:
            print("Invalid input. Try again: ")
    if lives == 0:
        print("Sorry you died")
    else:
        print("You have guessed the word '",word,"' correcly")

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
        hangman()
        
    elif gamenum == 3:
        def ttt():
            pass

    
