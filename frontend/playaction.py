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
import queue
from main import *

def pipeRemoveThread(queue):
    while(True):
        pipeBlob = pipeRemove()
        parts = pipeBlob.split('/')
        playerToAwardTen = parts[0]
        print(f"Player to award ten: {playerToAwardTen}")
        queue.put(playerToAwardTen)

def drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, redPlayer, redPlayerScores):
    
        for row in range(15):
            RowRedRect = []
            for col in range(2):
                x = col * rectWidth + 3 #determine x coordinate for each rectangle
                y = row * rectHeight + 78 #determine y coordinate for each rectangle
                rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw red rectangle
                RowRedRect.append(rect)
                if col == 0 and row < len(redPlayer):
                    textWords = redPlayer[row] #red player name
                if col == 1 and row < len(redPlayer):
                    textWords = str(redPlayerScores[redPlayer[row]]) #score of that particular red player
                if row >= len(redPlayer):
                    textWords = " "
                text = coolFont.render(textWords, True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                # Blit text onto the screen
                screen.blit(text, text_rect)
                
            RedTable.append(RowRedRect)

def drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, greenPlayer, greenPlayerScores):
        for row in range(15):
            RowGreenRect = []
            for col in range(2):
                x = col * rectWidth + 3 + screen.get_width() / 2 #determine x coordinate for each rectangle
                y = row * rectHeight + 78 #determine y coordinate for each rectangle
                rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw green rectangle
                if col == 0 and row < len(greenPlayer):
                    textWords = greenPlayer[row] #green player name
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

def playCountdownMusic():
    pygame.mixer.quit()
    pygame.mixer.init()
    track_number = random.randint(1, 8)  # Randomly select a track number between 1 and 8
    track_name = f"photon_tracks/Track{track_number:02d}.mp3"
    print(track_name)
    pygame.mixer.music.load(track_name)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

#Create a queue for communication between threads. 
#We need this to pass the gameplay events to the main program.
eventQueue = queue.Queue()

#Continuously read events from the pipe in a separate thread
pipeRemover = threading.Thread(target=pipeRemoveThread, args=(eventQueue,))
pipeRemover.start()

playerToAwardTen = ""
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

counterStartTimer = False
halfSpeedCountdown = True
timer30sec = 0
timer6min = 1
timerState = timer30sec
totalTime = 40
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

# playCountdownMusic()

redPlayerScores = {}
greenPlayerScores = {}

lock = threading.Lock() #Lock to ensure score dicts are not sorted while the scores are being updated


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

    if not eventQueue.empty():
            playerToAwardTen = eventQueue.get()
            for currRed in redPlayer:
                if currRed == playerToAwardTen:
                    redPlayerScores[currRed] += 10
            for currGreen in greenPlayer:
                if currGreen == playerToAwardTen:
                    greenPlayerScores[currGreen] += 10

    #Sort the redPlayerScores dict
    sorted_red_scores = dict(sorted(redPlayerScores.items(), key=lambda item: item[1]))
    
    #Create a reversed list of the sorted keys
    sorted_red_scores_keys = list(sorted_red_scores.keys())
    sorted_red_scores_keys.reverse()
    print(f'sorted_red_scores_keys: {sorted_red_scores_keys}')

    #Create a reversed list of the sorted values
    sorted_red_scores_values = list(sorted_red_scores.values())
    sorted_red_scores_values.reverse()
    print(f'sorted_red_scores_values: {sorted_red_scores_values}')

    #Sort the greenPlayerScores dict
    sorted_green_scores = dict(sorted(greenPlayerScores.items(), key=lambda item: item[1]))
    
    #Create a reversed list of the sorted keys
    sorted_green_scores_keys = list(sorted_green_scores.keys())
    sorted_green_scores_keys.reverse()
    print(f'sorted_green_scores_keys: {sorted_green_scores_keys}')
    
    #Create a reversed list of the sorted values
    sorted_green_scores_values = list(sorted_green_scores.values())
    sorted_green_scores_values.reverse()
    print(f'sorted_green_scores_values: {sorted_green_scores_values}')
    

    drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, sorted_red_scores_keys, sorted_red_scores)
    drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, sorted_green_scores_keys, sorted_green_scores)

    currentTime = (pygame.time.get_ticks() - startTime) / 1000
    if currentTime >= 22 and not counterStartTimer:
        playCountdownMusic()
        counterStartTimer = True
        # startTime = pygame.time.get_ticks() - (currentTime * 0.75) * 1000  # Adjust the starting time for the half-speed countdown
    if halfSpeedCountdown:
        countdownSpeed = 0.75
    else:
        countdownSpeed = 1
    if timerState == timer30sec and currentTime >= totalTime:
        timerState = timer6min
        totalTime = 360
        halfSpeedCountdown = False
        startTime = pygame.time.get_ticks()
    elif timerState == timer6min and currentTime >= totalTime:
        done = True
    remainingTime = max(0, totalTime - currentTime)
    remainingTime *= countdownSpeed
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