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
import main
from playerEntryScreenTables import drawLeftTable, drawRightTable
from playentry import *




should_continue = True
def pipeRemoveThread(queue, killFeed):
    global should_continue
    while should_continue:
        try:
            pipeBlob = pipeRemove()
            if pipeBlob:
                parts = pipeBlob.split(':')
                shooter = parts[0]
                target = parts[1]
                killFeed.append(f"{shooter} shot {target}")
                queue.put(shooter)
            else:
                continue
        except TimeoutError:
            continue

def drawKillFeed(killFeed, rect, screen, coolFont):
    startY = rect.top
    lineHeight = 20
    for i, entry in enumerate(killFeed):
        text = coolFont.render(entry, True, WHITE)
        text_rect = text.get_rect(topleft=(rect.left, startY + i * lineHeight))
        screen.blit(text, text_rect)
        
# def drawKillFeed(killFeed, rect, screen, coolFont):
#     # for i in range(len(killFeed)):
#     textWords = str(killFeed)
#     text = coolFont.render(textWords, True, WHITE)
#     text_rect = text.get_rect(center=rect.center)
#     screen.blit(text, text_rect)
#     return

# def pipeRemoveThread(queue, killFeed):
#     global should_continue
#     while should_continue:
#         try:
#             pipeBlob = pipeRemove()  # Timeout after 1 second
#             if pipeBlob:
#                 parts = pipeBlob.split(':')
#                 playerToAwardTen = parts[0]
#                 print(f"Player to award ten: {playerToAwardTen}")
#                 queue.put(playerToAwardTen)
#                 killFeed.append(pipeBlob)
#             else:
#                 continue  # Continue checking the while condition
#         except TimeoutError:
#             continue


def drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, redPlayer, redPlayerScores, flash):
    
        for row in range(15):
            RowRedRect = []
            for col in range(3):
                x = col * rectWidth + 3 #determine x coordinate for each rectangle
                y = row * rectHeight + 78 #determine y coordinate for each rectangle
                rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw red rectangle
                RowRedRect.append(rect)
                if col == 0 and row < len(redPlayer):
                    textWords = "B"
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 1 and row < len(redPlayer):
                    textWords = redPlayer[row] #red player name
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 2 and row < len(redPlayer):
                    textWords = str(redPlayerScores[redPlayer[row]]) #score of that particular red player
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 2 and row == 0:
                    if redPlayerScores[redPlayer[0]] != 0:
                        textWords = str(redPlayerScores[redPlayer[0]])
                        if flash % 2 == 0:
                            text = coolFont.render(textWords, True, WHITE)
                        if flash % 2 == 1:
                            text = coolFont.render(textWords, True, YELLOW)
                if row >= len(redPlayer):
                    textWords = " "
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                
                # Blit text onto the screen
                screen.blit(text, text_rect)
              
            RedTable.append(RowRedRect)

def drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, greenPlayer, greenPlayerScores, flash):
        for row in range(15):
            RowGreenRect = []
            for col in range(3):
                x = col * rectWidth + 3 + screen.get_width()/2 #determine x coordinate for each rectangle
                y = row * rectHeight + 78 #determine y coordinate for each rectangle
                rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, BLACK, BLACK) #draw green rectangle
                if col == 0 and row < len(greenPlayer):
                    textWords = "B"
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 1 and row < len(greenPlayer):
                    textWords = greenPlayer[row] #green player name
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 2 and row < len(greenPlayer):
                    textWords = str(greenPlayerScores[greenPlayer[row]])
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                if col == 2 and row == 0:
                    if greenPlayerScores[greenPlayer[0]] != 0:
                        textWords = str(greenPlayerScores[greenPlayer[0]])
                        if flash % 2 == 0:
                            text = coolFont.render(textWords, True, WHITE)
                        if flash % 2 == 1:
                            text = coolFont.render(textWords, True, YELLOW)
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

#List to store the full events from the pipe
killFeed = []

#Continuously read events from the pipe in a separate thread
pipeRemover = threading.Thread(target=pipeRemoveThread, args=(eventQueue, killFeed))
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

textFlashCount = 0

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
rectWidth = 885/6
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
redTotalScore = 0
greenTotalScore = 0

# playCountdownMusic()

redPlayerScores = {}
greenPlayerScores = {}

lock = threading.Lock() #Lock to ensure score dicts are not sorted while the scores are being updated

InputColorActive = pygame.Color('lightskyblue3')
InputColorPassive = pygame.Color('chartreuse4')
InputBoxColor = InputColorPassive
active = False
inputField = 0
numPlayers = 0
idWords = "Please Enter Player ID. Press Enter Key to Submit"
inputBox = pygame.Rect(screen.get_width()/2 - screen.get_width()/4, screen.get_height()/2 + 300, screen.get_width()/2, 40)
start = time.time()
RedTable = []
GreenTable = []

id = ''
codename = ''
numPlayers = 1
addedID = ''
addedCodeName = ''
entryCondition = False

def character_lim(codename):
    while len(codename) > 12:
        error_lim = "Please enter a codename 12 characters or less."


listNotEmpty = False
textWords = ''


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
                    redTotalScore = redTotalScore + 10
            for currGreen in greenPlayer:
                if currGreen == playerToAwardTen:
                    greenPlayerScores[currGreen] += 10
                    greenTotalScore = greenTotalScore + 10

    #Sort the redPlayerScores dict
    sorted_red_scores = dict(sorted(redPlayerScores.items(), key=lambda item: item[1]))
    
    #Create a reversed list of the sorted keys
    sorted_red_scores_keys = list(sorted_red_scores.keys())
    sorted_red_scores_keys.reverse()
    #print(f'sorted_red_scores_keys: {sorted_red_scores_keys}')

    #Create a reversed list of the sorted values
    sorted_red_scores_values = list(sorted_red_scores.values())
    sorted_red_scores_values.reverse()
    #print(f'sorted_red_scores_values: {sorted_red_scores_values}')
    

    #Sort the greenPlayerScores dict
    sorted_green_scores = dict(sorted(greenPlayerScores.items(), key=lambda item: item[1]))
    
    #Create a reversed list of the sorted keys
    sorted_green_scores_keys = list(sorted_green_scores.keys())
    sorted_green_scores_keys.reverse()
    #print(f'sorted_green_scores_keys: {sorted_green_scores_keys}')
    
    #Create a reversed list of the sorted values
    sorted_green_scores_values = list(sorted_green_scores.values())
    sorted_green_scores_values.reverse()
    #print(f'sorted_green_scores_values: {sorted_green_scores_values}')
   
    textFlashCount += 1
    drawLeftPlayTable(rectWidth, rectHeight, screen, coolFont, rect, RedTable, sorted_red_scores_keys, sorted_red_scores, textFlashCount)
    drawRightPlayTable(rectWidth, rectHeight, screen, coolFont, rect, GreenTable, sorted_green_scores_keys, sorted_green_scores, textFlashCount)

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
        totalTime = 5
        halfSpeedCountdown = False
        startTime = pygame.time.get_ticks()
    elif timerState == timer6min and currentTime >= totalTime:

        entryCondition = True
        redPlayer.clear()
        greenPlayer.clear()
        jsonObject = json.dumps(playRedPlayers)
        with open("redPlayers.json", "w") as outfile:
            outfile.write(jsonObject)
        jsonObject = json.dumps(playGreenPlayers)
        with open("greenPlayers.json", "w") as outfile:
            outfile.write(jsonObject)
        # done = True
    remainingTime = max(0, totalTime - currentTime)
    remainingTime *= countdownSpeed
    minutes = int(remainingTime) // 60
    seconds = int(remainingTime) % 60
    timeText = f"{minutes:02d}:{seconds:02d}"
    
 
    if redTotalScore > greenTotalScore:
        if textFlashCount % 2 == 0:
            redTotalScoreDisplay = DisplayBoxFont.render(str(redTotalScore), True, YELLOW)
            greenTotalScoreDisplay = DisplayBoxFont.render(str(greenTotalScore), True, WHITE)
        elif textFlashCount % 2 == 1:
            redTotalScoreDisplay = DisplayBoxFont.render(str(redTotalScore), True, BLACK)
            greenTotalScoreDisplay = DisplayBoxFont.render(str(greenTotalScore), True, WHITE)
    else:
        if textFlashCount % 2 == 0:
            greenTotalScoreDisplay = DisplayBoxFont.render(str(greenTotalScore), True, YELLOW)
            redTotalScoreDisplay = DisplayBoxFont.render(str(redTotalScore), True, WHITE)
        elif textFlashCount % 2 == 1:
            greenTotalScoreDisplay = DisplayBoxFont.render(str(greenTotalScore), True, BLACK)
            redTotalScoreDisplay = DisplayBoxFont.render(str(redTotalScore), True, WHITE)
    if redTotalScore == greenTotalScore:
        redTotalScoreDisplay = DisplayBoxFont.render(str(redTotalScore), True, WHITE)
        greenTotalScoreDisplay = DisplayBoxFont.render(str(greenTotalScore), True, WHITE)

    #Red & Green team text rendering
    redText = DisplayBoxFont.render("Red Team", True, RED) # Red Team
    redTeamScoreText = DisplayBoxFont.render("Red Team Score: ", True, RED) 
    
    screen.blit(redText,(screen.get_width()/4 - screen.get_width()/18, 12))
    screen.blit(redTeamScoreText,(screen.get_width()/15 - screen.get_width()/18, 40))
    screen.blit(redTotalScoreDisplay, (screen.get_width()/3 - screen.get_width()/20, 40))
    greenText = DisplayBoxFont.render("Green Team", True, GREEN) # Green Team
    greenTeamScoreText = DisplayBoxFont.render("Green Team Score: ", True, GREEN) 

    screen.blit(greenText,(screen.get_width() - screen.get_width()/4 - screen.get_width()/14, 12))
    screen.blit(greenTeamScoreText,(screen.get_width() - screen.get_width()/2.35, 40))
    screen.blit(greenTotalScoreDisplay, (screen.get_width() - screen.get_width()/18, 40))
    
    #Timer rendering
    pygame.draw.rect(screen, BLUE, countDownBox)
    timer = countDownFont.render(timeText, True, WHITE)
    countDownBoxRect = timer.get_rect(center=countDownBox.center)
    screen.blit(timer, countDownBoxRect)

    #Kill feed rendering
    killFeedBox = pygame.Rect(0, 378, 900, 320)
    pygame.draw.rect(screen, BLUE, killFeedBox, 1)
    pygame.draw.rect(screen, BLACK, killFeedBox.inflate(-2, -2))
    killFeedWords = '\n'.join(killFeed)
    startY = killFeedBox.top
    lineHeight = 20
    for i, entry in enumerate(killFeed):
        text = coolFont.render(entry, True, WHITE)
        text_rect = text.get_rect(topleft=(killFeedBox.left, startY + i * lineHeight))
        screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)

    # if entryCondition:
    #     screen.fill(BLACK)
    # while entryCondition:
    #     pygame.key.set_repeat(500, 25) #set up repeat entry from key holding
    #     screen.fill(BLACK)
    #     # rectWidth = 900/4
    #     # rectHeight = 580/16
    #     redRects = [[None] * 2 for _ in range(16)]
    #     greenRects = [[None] * 2 for _ in range(16)]

    #     drawLeftTable(RedTable, listNotEmpty, RedTeam, coolFont, screen, BLACK, RED, WHITE, textWords)

    #     drawRightTable(GreenTable, listNotEmpty, GreenTeam, coolFont, screen, BLACK, GREEN, WHITE, textWords)

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             exitProgram = True
    #             inEntryScreen = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if inputBox.collidepoint(event.pos):
    #                 active = True
    #             else:
    #                 active = False
    #         if event.type == pygame.KEYUP:
    #             if event.key == pygame.K_BACKSPACE:
    #                 userInput = userInput[:-1]

    #             elif event.key == pygame.K_MINUS:
    #                 RedTeam.redPlayers.clear()
    #                 GreenTeam.greenPlayers.clear()
    #                 playRedPlayers.clear()
    #                 playGreenPlayers.clear()
    #                 jsonObject = json.dumps(playRedPlayers)
    #                 with open("redPlayers.json", "w") as outfile:
    #                     outfile.write(jsonObject)
    #                 jsonObject = json.dumps(playGreenPlayers)
    #                 with open("greenPlayers.json", "w") as outfile:
    #                     outfile.write(jsonObject)
    #             elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
    #                 entryCondition = False
                    
    #             else:
    #                 if (event.key != pygame.K_RETURN):
    #                     userInput += event.unicode
                        
    #                 elif (event.key == pygame.K_RETURN):
                        
    #                     if len(userInput) <= 10: 
    #                         if (inputField == 0):
    #                             fetchData = (supabase.table('player').select("*").eq('id', userInput).execute())
    #                             print("fetchData = " + str(fetchData))
    #                             data = fetchData.data
    #                             key1 = "none"
    #                             if (data):
    #                                 key1 = data[0]['id']
    #                                 key2 = data[0]['codename']
    #                                 print ("outside if statement. key = " + str(key) + " userInput = " + userInput)

    #                                 if (userInput == str(key1)):

    #                                     # used to check if id is in table already
    #                                     rLength = len(RedTeam.redPlayers)
    #                                     gLength = len(GreenTeam.greenPlayers)
    #                                     print(rLength)
    #                                     print(gLength)
    #                                     for i in range(rLength):
    #                                         if(RedTeam.redPlayers[i].id == str(key1)):
    #                                             inputField = 0
    #                                             idWords = "               ID in table. Please Enter New ID"
    #                                             userInput = ""
    #                                             # break
    #                                     for k in range(gLength):
    #                                         if(GreenTeam.greenPlayers[k].id == str(key1)):
    #                                             inputField = 0
    #                                             idWords = "               ID in table. Please Enter New ID"
    #                                             userInput = ""
    #                                             # break

    #                                     if (userInput != ""):
    #                                         # if not in the table finds codename and prompts for machine code
    #                                         addedCodeName = str(key2)
    #                                         print("ID already exists, please input a new ID.") 
    #                                         addedID = str(key1)                          
    #                                         print(addedID)
    #                                         print(addedCodeName)
    #                                         idWords = "         ID found, please input a Machine Code."
    #                                         userInput = ""
    #                                         inputField = 2
    #                                         #print("Welcome back {codeName}")
    #                                         #supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute()  
    #                                         print("inside if statement " + " userInput = " + userInput + " key = " + str(key1))
                                    
    #                             elif ((userInput != str(key)) and (userInput != "") and (inputField == 0)):                           
    #                                 print("Welcome to the battlefield, enter your codename.")
    #                                 idWords = "Please Enter Code Name. Press Enter Key to Submit"

    #                                 #Character limit for codenames
    #                                 character_lim(codename)
                                    
    #                                 if ((userInput != "") and (inputField == 0)):
    #                                     addPlayer = supabase.table('player').insert({ 'id': userInput}).execute()
    #                                     inputField = 1
    #                                     #set the addedID equal to the userInput
    #                                     addedID = userInput
    #                                     userInput = ""
    #                                 elif ((userInput != "") and (inputField == 1)):
    #                                     supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute() 

    #                         if (inputField == 1) and (userInput != ""):
    #                             supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute()
    #                             fetchCodeName = supabase.table('player').select("codename").eq('id', addedID).execute()
    #                             print(fetchCodeName)
    #                             addedCodeName = userInput
    #                             inputField = 2
    #                             idWords = "Please Enter Machine Code. Press Enter Key to Submit"
    #                             userInput = ""
    #                             numPlayers += 1
    #                             #data_to_be_displayed = supabase.table('player').select("id").eq('id', addedID).execute()
    #                             response = supabase.table('player').select("*").eq('id', addedID).execute()
    #                             print(numPlayers)
    #                             # Extract the data part of the response
    #                             data = response.data

    #                             #Assuming there's at least one result and you want the first one
    #                             if data:
    #                                 codename = data[0]['codename']
    #                                 id = data[0]['id']
    #                                 print(codename)
    #                                 print(id)
                                
    #                             else:
    #                                 print("No data found.")

    #                         if (inputField == 2) and (userInput == ""):
    #                             while(event.key != pygame.K_RETURN):
    #                                 if event.type == pygame.KEYUP:
    #                                     if event.key == pygame.K_BACKSPACE:
    #                                         userInput = userInput[:-1]
    #                                 if event.type == pygame.QUIT:
    #                                     exitProgram = True
    #                                     inEntryScreen = False
    #                                 if event.key == pygame.K_MINUS:
    #                                     RedTeam.redPlayers.clear()
    #                                     GreenTeam.greenPlayers.clear()
    #                                     playRedPlayers.clear()
    #                                     playGreenPlayers.clear()
    #                                     jsonObject = json.dumps(playRedPlayers)
    #                                     with open("redPlayers.json", "w") as outfile:
    #                                         outfile.write(jsonObject)
    #                                     jsonObject = json.dumps(playGreenPlayers)
    #                                     with open("greenPlayers.json", "w") as outfile:
    #                                         outfile.write(jsonObject)
    #                                 if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
    #                                     exitProgram = True
    #                                     inEntryScreen = False
    #                                 else:
    #                                     userInput += event.unicode

    #                         if (inputField == 2) and (userInput != ""):
    #                             rLength = len(RedTeam.redPlayers)
    #                             gLength = len(GreenTeam.greenPlayers)
    #                             for i in range(rLength):
    #                                 if(RedTeam.redPlayers[i].id == addedID):
    #                                     inputField = 0
    #                                     idWords = "Please Enter Player ID. Press Enter Key to Submit"
    #                                     userInput = ""
                                        
    #                                     # break
    #                             for k in range(gLength):
    #                                 if(GreenTeam.greenPlayers[k].id == addedID):
    #                                     inputField = 0
    #                                     idWords = "Please Enter Player ID. Press Enter Key to Submit"
    #                                     userInput = ""
                                        
    #                                     # break
    #                             if (inputField != 0):
    #                                 listNotEmpty = True
    #                                 if (int(userInput) % 2 != 0):
    #                                     newPlayer = RedTeam(addedID, addedCodeName, userInput)
    #                                     RedTeam.redPlayers.append(newPlayer)
    #                                     playRedPlayers.append(addedCodeName)
    #                                     jsonObject = json.dumps(playRedPlayers)
    #                                     with open("redPlayers.json", "w") as outfile:
    #                                         outfile.write(jsonObject)
    #                                 if (int(userInput) % 2 == 0):
    #                                     newPlayer = GreenTeam(addedID, addedCodeName, userInput)
    #                                     GreenTeam.greenPlayers.append(newPlayer)
    #                                     playGreenPlayers.append(addedCodeName)
    #                                     jsonObject = json.dumps(playGreenPlayers)
    #                                     with open("greenPlayers.json", "w") as outfile:
    #                                         outfile.write(jsonObject)
    #                                 userInput = "Hardware/" + userInput + "/" + addedCodeName
                                    
    #                                 send_udp_packet(userInput)
    #                                 idWords = "Please Enter Player ID. Press Enter Key to Submit"
    #                                 inputField = 0
    #                                 userInput = ""    
    #                     else:
    #                         idWords = "Please Enter an ID no more than 10 characters"


def main():
    print("Hello World")
    


        
if __name__ == "__main__":
    main()