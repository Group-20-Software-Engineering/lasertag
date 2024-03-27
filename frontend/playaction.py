import sys
import random
import time
import pygame
import textwrap
pygame.init()
import os
from send import send_udp_packet, pipeRemove
import json
import threading
from main import *

def pipeRemoveThread() -> str:
    while(True):
        pipeBlob = pipeRemove()
        parts = pipeBlob.split('/')
        playerToAwardTen = parts[0]
        print(playerToAwardTen)
        return playerToAwardTen


def updatePlayAction(playerToAwardTen, redPlayer, greenPlayer, rectWidth, rectHeight, screen, coolFont, rect, RedTable, GreenTable):
    for currRed in redPlayer:
        if currRed == playerToAwardTen:
            redPlayerScores[currRed] += 10
    for currGreen in greenPlayer:
        if currGreen == playerToAwardTen:
            greenPlayerScores[currGreen] += 10
    drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable)
    drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable)

def drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, jsonRedObject, redPlayer, redPlayerScores):
    for row in range(15):
        RowRedRect = []
        for col in range(2):
            x = col * rectWidth + 3 #determine x coordinate for each rectangle
            y = row * rectHeight + 78 #determine y coordinate for each rectangle
            rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw red rectangle
            RowRedRect.append(rect)
            if col == 0 and row < len(redPlayer):
                textWords = jsonRedObject[row] #red player name
            if col == 1 and row < len(redPlayer):
                textWords = str(redPlayerScores[redPlayer[row]]) #score of that particular red player
            if row >= len(redPlayer):
                textWords = " "
            text = coolFont.render(textWords, True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            # Blit text onto the screen
            screen.blit(text, text_rect)
            
        RedTable.append(RowRedRect)

def drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, jsonGreenObject, greenPlayer, greenPlayerScores):
    for row in range(15):
        RowGreenRect = []
        for col in range(2):
            x = col * rectWidth + 3 + screen.get_width() / 2 #determine x coordinate for each rectangle
            y = row * rectHeight + 78 #determine y coordinate for each rectangle
            rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw green rectangle
            if col == 0 and row < len(greenPlayer):
                textWords = jsonGreenObject[row] #green player name
            if col == 1 and row < len(greenPlayer):
                textWords = str(greenPlayerScores[greenPlayer[row]])
            if row >= len(greenPlayer):
                textWords = " "
            text = coolFont.render(textWords, True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            # Blit text onto the screen
            screen.blit(text, text_rect)
            
        GreenTable.append(RowGreenRect)
    
def drawRect(row, col, x, y, rectWidth, rectHeight, screen, borderColor, fillColor) -> pygame.Rect:
    rect = pygame.Rect(x, y, rectWidth, rectHeight)
    pygame.draw.rect(screen, borderColor, rect, 1)
    pygame.draw.rect(screen, fillColor, rect.inflate(-2, -2))
    return rect

playerToAwardTen = threading.Thread(target=pipeRemoveThread)
playerToAwardTen.start()
pygame.key.set_repeat(500, 100)
coolFontName = "8-bit.ttf"
defFontName = "freesansbold.ttf"
coolFont = pygame.font.Font(coolFontName, 12)
countDownFont = pygame.font.Font(coolFontName, 18)
DisplayBoxFont = pygame.font.Font(coolFontName, 14) 
defFont = pygame.font.Font(defFontName, 24)

WHITE = (255, 255, 255)
BLUE = (0, 71, 171)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (125, 19, 19)
GREEN = (32, 87, 60)
clock = pygame.time.Clock()
size = (900,700)

pygame.display.set_caption("Photon -1: The Sequel (Laser Boogaloo)")
screen = pygame.display.set_mode(size)
countDownBox = pygame.Rect(screen.get_width()/2 - screen.get_width()/18, screen.get_height()/40,100,40)
done = False
redplayerCount = 0

timer30sec = 0
timer6min = 1
timerState = timer30sec
totalTime = 30
rectWidth = 885/4
rectHeight = 310/16
RedTable = []
GreenTable = []
startTime = pygame.time.get_ticks()
with open('redPlayers.json', 'r') as openfile:
    jsonRedObject = json.load(openfile)
with open('greenPlayers.json', 'r') as openfile:
    jsonGreenObject = json.load(openfile)
redPlayer = []
greenPlayer = []
redPlayer = jsonRedObject
greenPlayer = jsonGreenObject

redPlayerScores = {}
greenPlayerScores = {}

#Initialize the scores to 0
for currRed in redPlayer:
    redPlayerScores[currRed] = 0
for currGreen in greenPlayer:
    greenPlayerScores[currGreen] = 0

while not done:
    screen.fill(BLACK)
    rect = pygame.Rect(0, 75, 448, 300)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    rect = pygame.Rect(screen.get_width() / 2 + 2, 75, 448, 300)
    pygame.draw.rect(screen, GREEN, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            redPlayer.clear()
            greenPlayer.clear()
            jsonObject = json.dumps(playRedPlayers)
            with open("redPlayers.json", "w") as outfile:
                outfile.write(jsonObject)
            jsonObject = json.dumps(playGreenPlayers)
            with open("greenPlayers.json", "w") as outfile:
                outfile.write(jsonObject)
            done = True
    
    # for currRed in redPlayer:
    #     if currRed == playerToAwardTen:
    #         redPlayerScores[currRed] += 10
    # for currGreen in greenPlayer:
    #     if currGreen == playerToAwardTen:
    #         greenPlayerScores[currGreen] += 10
    
    # updatePlayAction(redPlayer, greenPlayer, rectWidth, rectHeight, screen, coolFont, rect, RedTable, GreenTable)
    for currRed in redPlayer:
        if currRed == playerToAwardTen:
            redPlayerScores[currRed] = redPlayerScores[currRed] + 10
    for currGreen in greenPlayer:
        if currGreen == playerToAwardTen:
            greenPlayerScores[currGreen] += 10
    #Print the scores
    # for r in redPlayer:
    #     print(f"Red player #{r}\'s score is {redPlayerScores[r]}")
    # for g in greenPlayer:
    #     print(f"Green player #{g}\'s score is {greenPlayerScores[g]}")

    drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, jsonRedObject, redPlayer, redPlayerScores)
    drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, jsonGreenObject, greenPlayer, greenPlayerScores)

    currentTime = (pygame.time.get_ticks() - startTime) / 1000
    if timerState == timer30sec and currentTime >= totalTime:
        timerState = timer6min
        totalTime = 360
        startTime = pygame.time.get_ticks()
    elif timerState == timer6min and currentTime >= totalTime:
        done = True
    remainingTime = max(0, totalTime - currentTime)
    minutes = int(remainingTime) // 60
    seconds = int(remainingTime) % 60
    timeText = f"{minutes:02d}:{seconds:02d}"

    redText = DisplayBoxFont.render("Red Team", True, RED) # Red Team
    screen.blit(redText,(screen.get_width()/4 - screen.get_width()/18, 12))
    greenText = DisplayBoxFont.render("Green Team", True, GREEN) # Green Team
    screen.blit(greenText,(screen.get_width() - screen.get_width()/4 - screen.get_width()/14, 12))
    pygame.draw.rect(screen, BLUE, countDownBox)
    timer = countDownFont.render(timeText, True, WHITE)
    countDownBoxRect = timer.get_rect(center=countDownBox.center)
    screen.blit(timer, countDownBoxRect)
    

    rect = pygame.Rect(0, 378, 900, 320)
    pygame.draw.rect(screen, BLUE, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    pygame.display.flip()
    clock.tick(60)

def main():
    print("Hello World")
    


        
if __name__ == "__main__":
    main()