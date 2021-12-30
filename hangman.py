import random
import time

words = ["mouse", "book", "paper", "bunny"]
word = random.choice(words)

initial = []
for letter in word:
    initial.append("_")
desired = list(word)

for x in initial:
    print(x + " ", end="")

guesses = []    
    
time.sleep(1)
trials = len(word) + 2
while trials > 0:
    user = input("Enter a letter: ")
    val = True
    
    #check to see whether this has been guessed yet
    for guess in guesses:
        if guess == user:
            print("\n\nYou have already guessed this letter!")
            val = False
    
    #print result
    if val == True:
        if user in desired:
            print("\n\nCorrect!")
        else:
            print("\n\nWrong!")
            trials -= 1
        
    #replace _ with letter
    for counter in range(0, len(desired)):
        if user == desired[counter]:
            initial[counter] = user
            
    #print the new list
    for x in initial:
        print(x, end=" ")
    
    #print the guesses so far
    if val == True:
        guesses.append(user)
    print("\nGuesses: ", guesses)
    
    #print the amount of trials left
    if trials != 1:
        print("There are", trials, "trials left")
    else:
        print("There is", trials, "trial left")
    
    time.sleep(1)
    
    #check for winning or losing
    count = 0
    for counter in range(0, len(desired)):
        if initial[counter] == desired[counter]:
            count += 1
    if count == len(word):
        print("\nYou win!")
        break
    elif trials == 0:
        print("\nSorry, better luck next time!")
        print("The word was", word, "!")
