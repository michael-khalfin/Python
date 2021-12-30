from processing import *

width = 550
height = 600

cookie = {
    'x': 15,
    'y': 15,
    'w': 150,
    'h': 150
}

numCookies = 0
cookiesPerSec = 0

grandmaBtn = {
    'x': 55,
    'y': 200,
    'w': 120,
    'h': 25,
    'text': "Grandma",
    'amtPerSec': 1,
    'price': 10,
    'priceInc': 3,
    'owned': 0
}

farmBtn = {
    'x': 50,
    'y': 230,
    'w': 130,
    'h': 25,
    'text': "Farm",
    'amtPerSec': 30,
    'price': 100,
    'priceInc': 53,
    'owned': 0
}

restaurantBtn = {
    'x': 45,
    'y': 260,
    'w': 140,
    'h': 25,
    'text': "Restaurant",
    'amtPerSec': 50,
    'price': 200,
    'priceInc': 113,
    'owned': 0
}

chainBtn = {
    'x': 40,
    'y': 290,
    'w': 150,
    'h': 25,
    'text': "Chain",
    'amtPerSec': 80,
    'price': 1000,
    'priceInc': 600,
    'owned': 0
}

billgatesBtn = {
    'x': 35,
    'y': 320,
    'w': 160,
    'h': 25,
    'text': "Bill Gates",
    'amtPerSec': 200,
    'price': 10000,
    'priceInc': 6500,
    'owned': 0
}

btns = [grandmaBtn, farmBtn, restaurantBtn, chainBtn, billgatesBtn]

def drawButtons():
    for b in btns:
        # draw rectangle for button
        fill(255, 0, 0)
        stroke(255, 0, 0)
        rect(b['x'], b['y'], b['w'], b['h'])
        # draw text on button
        textSize(14)
        fill(255)
        text(b['text'] + ' - ' + str(b['price']), b['x'] + 18, b['y'] + 17)
        # draw text for amount of upgrade owned
        fill(0)
        textSize(20)
        text("Owned: " + str(b['owned']), 225, b['y'] + 20)
        
def calculatePassiveIncome():
    global cookiesPerSec
    total = 0
    for b in btns:
        total += b['owned'] * b['amtPerSec']
    cookiesPerSec = total

def setup():
    size(width, height)
    cookie['image'] = loadImage("http://cookie-clicker.oyosite.com/cookie.jpg")
    
    global lastSec
    lastSec = millis()
    
def draw():
    global numCookies, lastSec
    background(255, 255, 255)
    image(cookie['image'], cookie['x'], cookie['y'], cookie['w'], cookie['h'])
    
    textSize(24)
    fill(0, 0, 0)
    text("Cookies: " + str(numCookies), 200, 50)
    text("Cookies Per Second: " + str(cookiesPerSec), 200, 75)
    text("~ Happy Snacking! ~", 200, 420)
    drawButtons()
    calculatePassiveIncome()
    curr = millis()
    if curr > lastSec + 1000:
        numCookies += cookiesPerSec
        lastSec = curr
    
def mouseClicked():
    global numCookies, cookiesPerSec
    if (cookie['x'] <= mouse.x <= cookie['x'] + cookie['w'] and 
        cookie['y'] <= mouse.y <= cookie['y'] + cookie['h']):
        numCookies += 1
    for b in btns:
        if (b['x'] <= mouse.x <= b['x'] + b['w'] and 
            b['y'] <= mouse.y <= b['y'] + b['h']):
            if numCookies >= b['price']:
                numCookies -= b['price']
                b['price'] += b['priceInc']
                b['owned'] += 1
    
run()
