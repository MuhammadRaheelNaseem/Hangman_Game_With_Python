import random

name=input("Enter Your Name: ")
print(f"All the best: >>>>>> {name}")

words=['website','python','java','hangman','computer'] # make list for random choice for guessing

word=random.choice(words)
print()
print("Guest the characters")
guesses=""
turns=3
while True:
    failed=0
    print("Step !")
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print("_",end="")
            failed+=1  
    if failed==0:
        print("\n\nYou win!")
        print(f"\nThe word is: {word}")
        break
    guess=input("\n\nGuess the character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("\nWrong!")
        print(f"\nYou have {turns} more guesses")
        if turns==0:
            print('\n\nYou Loss!')
            print(f"The correct word is {word}")
            break
