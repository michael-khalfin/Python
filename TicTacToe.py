import random
import time

def Computer():
    time.sleep(1)
    print("Computers turn!")
    
    time.sleep(1)
    print("Computer plays")
    cont = True
    while cont == True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if myList[row][column] == " ":
            cont = False
            myList[row][column] = "o"
    
def User():
    print("User's turn")
    time.sleep(1)
    
    cont = True
    while cont == True:
        row = int(input("Enter a row"))
        column = int(input("Enter a column"))
        
        if row < 0 or row > 2:
            print("Enter a valid row number")
            time.sleep(1)
        elif column < 0 or column > 2:
            print("Enter a valid column number")
            time.sleep(1)
        elif myList [row] [column] != " ":
            print("This square has already been selected")
            time.sleep(1)
        else:
            cont = False
            myList [row] [column] = "x"
    
def Win():
    if myList [0] [0] == myList [0] [1] and myList [0] [0] == myList [0] [2] and myList [0] [0] != " ":
        return True
    elif myList [1] [0] == myList [1] [1] and myList [1] [0] == myList [1] [2] and myList [1] [0] != " ":
        return True
    elif myList [2] [0] == myList [2] [1] and myList [2] [0] == myList [2] [2] and myList [2] [0] != " ":
        return True
    elif myList [0] [0] == myList [1] [0] and myList [0] [0] == myList [2] [0] and myList [0] [0] != " ":
        return True
    elif myList [0] [1] == myList [1] [1] and myList [0] [1] == myList [2] [1] and myList [0] [1] != " ":
        return True
    elif myList [0] [2] == myList [1] [2] and myList [0] [2] == myList [2] [2] and myList [0] [2] != " ":
        return True
    elif myList [0] [0] == myList [1] [1] and myList [0] [0] == myList [2] [2] and myList [0] [0] != " ":
        return True
    elif myList [2] [0] == myList [1] [1] and myList [2] [0] == myList [0] [2] and myList [2] [0] != " ":
        return True
    else:
        return False

def DisplayBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            if j < 2:
                print(myList[i][j] + "|", end="")
            else:
                print(myList[i][j], end="")
        if i < 2:
            print("\n------")
    
myList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

win = False
counter = 0
while win == False:
    Computer()
    DisplayBoard()
    win = Win()
    if win == True:
        print("\nThe computer wins!")
        break
    counter += 1    
    
    if counter == 9:
        print("\nThere is a tie!")
        break
    
    print("\n")             
    User()
    DisplayBoard()
    win = Win()
    if win == True:
        print("\nYou win!")
    counter += 1
    
    print("\n")
