from processing import *
from random import randint
import webaudio

width = 540
height = 450
tile_size = 30
num_columns = (width/tile_size)
num_rows = (height/tile_size)

#18 columns, 15 rows

maze = [
    [1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 3, 1, 1, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 4, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 4, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 4, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 4, 1, 0, 1, 1],
    [1, 1, 1, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 4, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 3, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 3, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2, 1],
    [1, 1, 1, 0, 1, 0, 3, 0, 1, 0, 0, 0, 1, 5, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#0 - space to walk
#1 - wall
#2 - fire
#3 - portal
#4 - ice
#5 - start
#6 - end

player = {
    "row":13,
    "column":13
}

maxTime = 30
quadruple_time = 150
max_units = 150
direction = UP
ice = False

def findTeleports():
    global teleports
    teleports = []
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 3:
                t = {
                    'row': row,
                    'column': column
                }
                teleports.append(t)

def setup():
    size(width, height)
    
    global playerImage
    playerImage = loadImage("https://oyohub.s3.amazonaws.com/spriteeditor/projects/5dd46f32792ac26a61bc7be1/Maze-Project-1.png")
    
    global finishImage
    finishImage = loadImage("https://oyohub.s3.amazonaws.com/spriteeditor/projects/5dd46f32792ac26a61bc7be1/Maze-Project-2.png")
    
    global fireImage
    fireImage = loadImage("https://oyohub.s3.amazonaws.com/spriteeditor/projects/5dd46f32792ac26a61bc7be1/Maze-Project-3.png")
    
    global portalImage
    portalImage = loadImage("https://oyohub.s3.amazonaws.com/spriteeditor/projects/5dd46f32792ac26a61bc7be1/Maze-Project-4.png")
    
    global wallSound
    wallSound = webaudio.loadAudio("https://www.soundjay.com/button/sounds/button-10.mp3")
    
    global teleportSound
    teleportSound = webaudio.loadAudio("https://www.soundjay.com/button/sounds/button-8.mp3")
    findTeleports()
    
    global iceSound
    iceSound = webaudio.loadAudio("https://www.soundjay.com/button/sounds/button-16.mp3")
    
    global gameoverSound
    gameoverSound = webaudio.loadAudio("https://www.soundjay.com/button/sounds/button-7.mp3")
    
    global winSound
    winSound = webaudio.loadAudio("https://www.soundjay.com/button/sounds/button-14.mp3")

def draw():
    background(0, 153, 255)
    drawGrid()
    drawWalls()
    
    image(finishImage, tile_size+.6, .6, 29, 29)
    #blackout()
    
    drawTimer()
    image(playerImage, player["column"] * tile_size+.6, player["row"] * tile_size+.6, 29, 29)
    
    row = player['row']
    column = player['column']
    if maze[row][column] == 2:
        gameOver()
    elif maze[row][column] == 6:
        win()
    
def drawGrid():
    stroke(0, 107, 179)
    for x in range(0, width, tile_size):
        line(x, 0, x, height)
    for y in range(0, height, tile_size):
        line(0, y, width, y)
        
def drawWalls():
    for row in range(num_rows):
        for column in range(num_columns):
            if maze[row][column] == 1:
                stroke(0, 15, 26)
                fill(0, 46, 77)
                rect(tile_size * column, tile_size * row, tile_size, tile_size)
            elif maze[row][column] == 2:
                image(fireImage, column * tile_size+.6, row * tile_size+.6, 29, 29)
            elif maze[row][column] == 3:
                image(portalImage, column * tile_size+.6, row * tile_size+.6, 29, 29)
            elif maze[row][column] == 4:
                stroke(0, 15, 26)
                fill(0, 255, 255)
                rect(tile_size * column, tile_size * row, tile_size, tile_size)
    
def blackout():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if ((player['row'] != row or player['column'] != column) and
            (player['row'] != row+1 or player['column'] != column+1) and
            (player['row'] != row-1 or player['column'] != column-1) and
            (player['row'] != row or player['column'] != column+1) and
            (player['row'] != row or player['column'] != column-1) and
            (player['row'] != row+1 or player['column'] != column) and
            (player['row'] != row-1 or player['column'] != column) and
            (player['row'] != row-1 or player['column'] != column+1) and
            (player['row'] != row+1 or player['column'] != column-1)):
                stroke(0, 0, 0)
                fill(0, 0, 0)
                rect(column * tile_size, row * tile_size, tile_size, tile_size)
    
def movePlayer():
    if direction == UP:
        new_row = player["row"] - 1
        column = player["column"]
        if new_row >= 0 and maze[new_row][column] != 1:
            player["row"] = new_row
        else:
            wallSound.play()
    if direction == DOWN:
        new_row = player["row"] + 1
        column = player["column"]
        if new_row < num_rows and maze[new_row][column] != 1:
            player["row"] = new_row
        else:
            wallSound.play()
    if direction == RIGHT:
        row = player["row"]
        new_column = player["column"] + 1
        if new_column < num_columns and maze[row][new_column] != 1:
            player["column"] = new_column
        else:
            wallSound.play()
    if direction == LEFT:
        row = player["row"]
        new_column = player["column"] - 1
        if new_column >= 0 and maze[row][new_column] != 1:
            player["column"] = new_column
        else:
            wallSound.play()
    checkTeleports(player['row'], player['column'])

def keyPressed():
    global direction
    if keyboard.keyCode in [UP, DOWN, LEFT, RIGHT]:
        if ice == False:
            direction = keyboard.keyCode
            movePlayer()
        
def checkTeleports(row, column):
    myTeleport = None
    # check if the player is standing on a teleport
    for i in range(len(teleports)):
        t = teleports[i]
        if t['row'] == row and t['column'] == column:
            myTeleport = i
    if myTeleport is not None:
        teleportSound.play()
        # choose a random other teleport
        r = randint(0, len(teleports)-1)
        # keep choosing a random teleport in case we chose
        # the same one we are already standing on
        while r == myTeleport:
            r = randint(0, len(teleports)-1)
        # set the player's position to the location of the
        # chosen teleport
        player['row'] = teleports[r]['row']
        player['column'] = teleports[r]['column']
        
def checkIce(row, column):
    global ice
    if maze[row][column] == 4:
        iceSound.play()
        if direction == UP:
            new_row = player["row"] - 1
            if new_row >= 0 and maze[new_row][column] != 1:
                movePlayer()
                ice = True
        if direction == DOWN:
            new_row = player["row"] + 1
            if new_row < num_rows and maze[new_row][column] != 1:
                movePlayer()
                ice = True
        if direction == RIGHT:
            new_column = player["column"] + 1
            if new_column < num_columns and maze[row][new_column] != 1:
                movePlayer()
                ice = True
        if direction == LEFT:
            new_column = player["column"] - 1
            if new_column >= 0 and maze[row][new_column] != 1:
                movePlayer()
                ice = True
    else:
        ice = False
        
def drawTimer():
    milli = millis()
    seconds = milli/1000
    timeLeft = maxTime - seconds
    timeText = "Time Left: %02d" % (timeLeft)
    fill(255, 255, 255)
    textSize(15)
    text(timeText, 400, 20)
    
    if timeLeft == 0:
        gameOver()
    
    global quadruple_time, max_units
    units = milli/200
    valueChanged = quadruple_time != (max_units - units)
    quadruple_time = max_units - units
    if valueChanged:
        checkIce(player['row'], player['column'])
        
def gameOver():
    gameoverSound.play()
    fill(255, 0, 0)
    textSize(40)
    text("Game Over! \n Try Again!", 200, 200)
    exitp()
    
def win():
    winSound.play()
    fill(255, 0, 0)
    textSize(40)
    text("You Win!", 200, 200)
    exitp()

run()
