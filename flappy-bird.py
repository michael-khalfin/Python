from processing import *
from random import randint

width = 550
height = 420

bird = {
    'x': 50,
    'y': 200,
    'w': 20,
    'h': 14,
    'velx': 2
    }

pipes = []

delay = False
collisions = False
token = False
tokens = 0

score = 0
highScore = 0

can_restart = False

def generatePipes():
    global pipe_counter
    if pipe_counter == 0:
        global collisions
        collisions = True
        pipe_counter = 140
        pipe = {
            'x': 600,
            'w': 24,
            'h': 60,
            'image': {}
            }
        pipe['bottom'] = randint(1, 5)
        pipe['image']['bottom'] = loadImage("http://cookie-clicker.oyosite.com/toppipe_bottom.png")
        pipe['image']['bottom_bod'] = loadImage("http://cookie-clicker.oyosite.com/pipe_buttom.png")
        pipe['image']['upper'] = loadImage("http://cookie-clicker.oyosite.com/toppipe_upper.png")
        pipe['image']['upper_bod'] = loadImage("http://cookie-clicker.oyosite.com/pipe_upper.png")
        pipes.append(pipe)
    pipe_counter -= 1

def drawPipes():
    for pipe in pipes:
        for num in range(1, pipe['bottom']):
            y = height - pipe['h'] * num
            image(pipe['image']['bottom_bod'], pipe['x'], y, pipe['w'], pipe['h'])
        y = height - pipe['h'] * pipe['bottom']
        image(pipe['image']['bottom'], pipe['x'], y, pipe['w'], pipe['h'])
        for num in range(1, 6 - pipe['bottom']):
            y = pipe['h'] * (num - 1)
            image(pipe['image']['upper_bod'], pipe['x'], y, pipe['w'], pipe['h'])
        y = pipe['h'] * (5 - pipe['bottom'])
        image(pipe['image']['upper'], pipe['x'], y, pipe['w'], pipe['h'])
        
def movePipes():
    for pipe in pipes:
        pipe['x'] -= bird['velx']

def checkCollisions():
    global can_restart
    if pipes[0]['x'] <= 0:
        del pipes[0]
    
    y_top = pipes[0]['h'] * (5 - pipes[0]['bottom'])
    y_bottom = height - pipes[0]['h'] * pipes[0]['bottom']
    if ((bird['y'] < y_top + pipes[0]['h'] or
        bird['y'] > y_bottom - bird['h']) and
        (bird['x'] > pipes[0]['x'] - pipes[0]['w']/2 - bird['w']/2 and 
         bird['x'] < pipes[0]['x'] + pipes[0]['w']/2 + bird['w']/2)):
        can_restart = True
        
def groundCollisions():
    global can_restart
    if bird['y'] <= bird['h']:
        can_restart = True
    if bird['y'] >= height - bird['h']:
        can_restart = True
        
def calcScore():
    global score, token, token_delay, tokens
    if bird['x'] > pipes[0]['x'] - .5 and bird['x'] < pipes[0]['x'] + .5:
        score += 1
        if token == True:
            token = False
            token_delay = 60
            tokens += 1
        
def restart():
    global anim_counter
    anim_counter = 0
    bird['y'] = 200
    global pipes, collisions
    pipes = []
    collisions = False
    
    global score, highScore
    if score > highScore:
        highScore = score
    score = 0
    
    global token, token_delay, can_restart
    token = False
    token_delay = 60
    can_restart = False
    
def generateToken():
    y_bottom = height - pipes[0]['h'] * pipes[0]['bottom']
    image(tokenImage, pipes[0]['x'] + 5, y_bottom - 40, 22, 22)
    
def displayData():
    textSize(20)
    fill(255)
    text("Score: " + str(score), 20, 20)
    text("High Score: " + str(highScore), 20, 50)
    if tokens >= 1:
        image(tokenImage, 10, 395, 22, 22)
        text("5", 15, 390)
    if tokens >= 2:
        image(tokenImage, 50, 395, 22, 22)
        text("25", 50, 390)
    if tokens >= 3:
        image(tokenImage, 90, 395, 22, 22)
        text("50", 90, 390)
    if tokens >= 4:
        image(tokenImage, 130, 395, 22, 22)
        text("100", 125, 390)
    if tokens >= 5:
        image(tokenImage, 170, 395, 22, 22)
        text("500", 165, 390)
        
def birdAnimation():
    global anim_counter, curr_frame
    if anim_counter == 0:
        anim_counter = 10
        curr_frame = (curr_frame+1) % len(bird['image'])
    anim_counter -= 1
    
    image(bird['image'][curr_frame], bird['x'], bird['y'], bird['w'], bird['h'])

def setup():
    size(width, height)
    
    global anim_counter, curr_frame, pipe_counter
    bird['image'] = [loadImage("http://cookie-clicker.oyosite.com/flappybird.png"),
                     loadImage("http://cookie-clicker.oyosite.com/flappybird2.png"),
                     loadImage("http://cookie-clicker.oyosite.com/flappybird3.png"),
                     loadImage("http://cookie-clicker.oyosite.com/flappybird2.png")]
    anim_counter = 10
    curr_frame = 0
    pipe_counter = 20
    
    global bird_counter
    bird_counter = 10
    
    global tokenImage, token_delay
    tokenImage = loadImage("http://cookie-clicker.oyosite.com/token.png")
    # 22 by 22
    token_delay = 60
    
def draw():
    background(0, 102, 255)
    
    if not can_restart:
        birdAnimation()
        generatePipes()
        drawPipes()
        movePipes()
    
        global delay, bird_counter
        if not delay:
            bird['y'] += 2.8
        else:
            if bird_counter == 0:
                delay = False
            bird_counter -= 1
    else:
        fill(255)
        rect(100, 150, 370, 100)
        textSize(50)
        fill(255, 51, 0)
        text("GAME OVER", 130, height/2)
        textSize(20)
        text("PRESS ENTER TO RESTART", 150, height/2 + 30)
        
    if collisions == True:
        calcScore()
        checkCollisions()
    groundCollisions()
    
    global score, token, token_delay, tokens
    if ((score == 4 and tokens == 0)
        or (score == 24 and tokens == 1)
        or (score == 49 and tokens == 2)
        or (score == 99 and tokens == 3)
        or (score == 499 and tokens == 4)):
        token = True
    if token == True:
        if token_delay > 0:
            token_delay -= 1
    if token_delay == 0:
        generateToken()
    displayData()
    
def keyPressed():
    if keyboard.keyCode == ENTER: # enter key
        if can_restart:
            restart()        
    if keyboard.keyCode == 32: # space
        if not can_restart:
            bird['y'] -= 17
        
            global delay, bird_counter
            delay = True
            bird_counter = 10
    
run()
