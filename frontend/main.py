import json
import sys
import random
import time
import pygame
import textwrap
#import playaction as playaction

import os
from send import send_udp_packet

from supabase import create_client, Client 

def proceedToPlayerEntry():
    pygame.mixer.quit()
    pygame.mixer.init()
    pygame.mixer.music.load("player_entry.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

def playMusic():
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1)


def rocketAndText(screen, title, defFont, coolFont, y):
    rocketText = "        !\n        !\n        ^\n      /    \\\n    /____\\\n    |=    =|\n    |        |\n    |        |\n    |        |\n    |        |\n    |        |\n   /|##!##|\\\n  / |##!##| \\\n /  |##!##|  \\\n |  / ^ | ^ \\  |\n | /   ( | )   \\ |\n |/    ( | )    \\|\n      ((   ))\n     ((  :  ))\n     ((  :  ))\n      ((   ))\n       (( ))\n        ( )\n         |\n         |\n         |\n         |\n"
    blit_text(screen, rocketText, (screen.get_width()/2 - title.get_width()/2 + 185, 25 - y), defFont)
    screen.blit(title,(screen.get_width()/2 - title.get_width()/2, screen.get_height() - y))
    storyText = "\n\n      In a world where the Joestars\n         are now fighting in space!\n      You will now join the Joestars\n  Against the evil laser Stand Users\n       (which aren't actually lasers\n        but simpler infrared lights\n                  emitted as beams)\n                            KILL.\n\n      But your enemies are not weak...\n    They have their own unique stands\n            with powerful abilities.\n Dio has upgraded all his laser stand\n    users to FREEZE you upon damage.\n\n                  But do not fear!!!\n        As your uncle Jotaro Kujo\n With his stand STARRRR PLATINUM.\n            Has done the same to your\n                  laser stands too.\n\n         Do not be too overconfident.\n As when you reading this amazing text\n  Dio hired Sigma from Overwatch 2 D:\n                  With the power of\n        ''WHAT IS THAT MELODY?!?!''\n        Sigma fluxxed 99.99 percent\n             of the Joestar family.\n\nSo now it's up to you and your friends.\n      Oh wait you don't have friends...\n No worries, as your Jotaro will still\n  be with you on this massive journey.\n\n      WHAT ARE YOU WAITING FOR!!!\n    GO NOW BEFORE THE TIMER ENDS\n    GET THE WIN FOR THE JOESTARS\n        DO NOT LET THE ENEMY WIN\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                     What? NANI!\n   Did you find an easter egg yet??\n          Why are you still here?\n           What are you DOING!!!!\n            Why are we still here\n                 Just to suffer...\n                     BYEEEEEEE\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDo you not want to help the Joestars??\n  Well then, I would like to introduce\n          the sponsor of this project         \n                    RAID- wait what\n                    no no no... I mean\n                   OUR PET MASCOT        \n                       SHIPLEY!!!!!!!\n     for keeping team 20 sane for the\n                past few sprints :3     \n   Now you guys can go taste freedom\n    Thanks for reading this TedTalk."
    blit_text(screen, storyText, (screen.get_width()/2 - title.get_width()/2 - 40,screen.get_height() + title.get_height() - y), coolFont)
        
def circles(screen, color):
    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, color,(a,b), 2)

def write():
        x = 1

def setup():
    url: str = "https://jmfukmeanfezxzgrsitj.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptZnVrbWVhbmZlenh6Z3JzaXRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNTEyMDMsImV4cCI6MjAyMjgyNzIwM30.r99dqev77H1YPfAudZ9xm5heBt-jR-dNDiuI8-xVuZk"
    supabase: Client = create_client(url, key)
    pygame.init() #start the game
    pygame.key.set_repeat(500, 25) #set up repeat entry from key holding
    currentDir = os.getcwd() #establish working directory
    coolFontName = "8-bit.ttf" #cool font
    defFontName = "freesansbold.ttf" #default font
    coolFont = pygame.font.Font(coolFontName, 18)
    inputBoxFont = pygame.font.Font(coolFontName, 14) 
    defFont = pygame.font.Font(defFontName, 24)
    WHITE = (255, 255, 255)
    BLUE = (0, 71, 171)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    RED = (125, 19, 19)
    GREEN = (32, 87, 60)
    exitProgram = False
    exitIntroScreen = False
    inEntryScreen = False
    inPlayScreen = False
    idNamePairFound = True
    clock = pygame.time.Clock()
    size = (900,700)
    screen = pygame.display.set_mode(size)
    image_path = "logo.jpg"
    center = screen.get_rect().center
    pygame.display.set_caption("Photon")
    title = pygame.image.load(image_path).convert()
    title = pygame.transform.scale(title, (500,242)) 
    y = 0
    i = 1
    userInput = ''
    codeName = ''
    red_Id = []
    red_Code = []
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
    machineCode = ''
    class RedTeam:
            def __init__(red, id, codename, machineCode):
                red.id = id
                red.codename = codename
                red.machineCode = machineCode
            redPlayers = []
    class GreenTeam:
        def __init__(green, id, codename, machineCode):
            green.id = id
            green.codename = codename
            green.machineCode = machineCode
        greenPlayers = []
    listNotEmpty = False
    textWords = ''
    playMusic()
    while not exitIntroScreen:    
        #WHEN SENDING HARDWARE ID USE THE FORMAT "Hardware/ID" AS SEEN BELLOW
        # test = "Hardware/9"
        # send_udp_packet(test)
        screen.fill(BLACK)
        for i in range(5):
            circles(screen, WHITE)
        y = y + 1
        rocketAndText(screen, title, defFont, coolFont, y)
        end = time.time()
        total = end - start
        #If the time runs out, or the user skips through the intro screen, proceed to player entry screen.
        if (total > 150 or y > 6000):
            proceedToPlayerEntry()
            inEntryScreen = True
            exitIntroScreen = True
        #Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitProgram = True
                exitIntroScreen = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    print("Pressing Back")
                    print(y)
                    y = y - 60
                elif event.key == pygame.K_MINUS:
                    y = y + 60
        #Create the player entry screen
        while ((exitIntroScreen == True) and (inEntryScreen == True)):
            pygame.key.set_repeat(500, 25) #set up repeat entry from key holding
            screen.fill(BLACK)
            rectWidth = 900/4
            rectHeight = 580/16
            redRects = [[None] * 2 for _ in range(16)]
            greenRects = [[None] * 2 for _ in range(16)]

            for row in range(15):
                RowRedRect = []

                for col in range(2):
                    x = col * rectWidth
                    y = row * rectHeight + 44
                    rect = pygame.Rect(x, y, rectWidth, rectHeight)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                    pygame.draw.rect(screen, RED, rect.inflate(-2, -2))
                    RowRedRect.append(rect)
                    if (len(RedTeam.redPlayers) == 0):
                        pass
                    elif (listNotEmpty == True):
                        if col == 0 and row < len(RedTeam.redPlayers):
                            textWords = RedTeam.redPlayers[row].id
                        if col == 1 and row < len(RedTeam.redPlayers):
                            textWords = RedTeam.redPlayers[row].codename
                        if row >= len(RedTeam.redPlayers):
                            textWords = " "
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                    # Blit text onto the screen
                    screen.blit(text, text_rect)
                    
                RedTable.append(RowRedRect)
            for row in range(15):
                RowGreenRect = []
                for col in range(2):
                    x = col * rectWidth + screen.get_width() / 2
                    y = row * rectHeight + 44
                    rect = pygame.Rect(x, y, rectWidth, rectHeight)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                    pygame.draw.rect(screen, GREEN, rect.inflate(-2, -2))
                    if (len(GreenTeam.greenPlayers) == 0):
                        pass
                    elif (listNotEmpty == True):
                        if col == 0 and row < len(GreenTeam.greenPlayers):
                            textWords = GreenTeam.greenPlayers[row].id
                        if col == 1 and row < len(GreenTeam.greenPlayers):
                            textWords = GreenTeam.greenPlayers[row].codename
                        if row >= len(GreenTeam.greenPlayers):
                            textWords = " "
                    text = coolFont.render(textWords, True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                    # Blit text onto the screen
                    screen.blit(text, text_rect)
                    
                GreenTable.append(RowGreenRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitProgram = True
                    inEntryScreen = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputBox.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        userInput = userInput[:-1]

                    elif event.key == pygame.K_MINUS:
                        RedTeam.redPlayers.clear()
                        GreenTeam.greenPlayers.clear()

                    elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        exitProgram = True
                        inEntryScreen = False
                        
                    else:
                        if (event.key != pygame.K_RETURN):
                            userInput += event.unicode
                            
                        elif (event.key == pygame.K_RETURN):
                            
                            if (inputField == 0):
                                fetchId = (supabase.table('player').select("id").eq('id', userInput).execute())
                                fetchCn = (supabase.table('player').select("*").eq('id', userInput).execute())
                                print("fetchId = " + str(fetchId))
                                ID_data = fetchId.data
                                Cn_data = fetchCn.data
                                key1 = "none"
                                if (ID_data):
                                    key1 = ID_data[0]['id']
                                    key2 = Cn_data[0]['codename']
                                    print ("outside if statement. key = " + str(key) + " userInput = " + userInput)

                                    if (userInput == str(key1)):

                                        # used to check if id is in table already
                                        rLength = len(RedTeam.redPlayers)
                                        gLength = len(GreenTeam.greenPlayers)
                                        print(rLength)
                                        print(gLength)
                                        for i in range(rLength):
                                            if(RedTeam.redPlayers[i].id == str(key1)):
                                                inputField = 0
                                                idWords = "               ID in table. Please Enter New ID"
                                                userInput = ""
                                                # break
                                        for k in range(gLength):
                                            if(GreenTeam.greenPlayers[k].id == str(key1)):
                                                inputField = 0
                                                idWords = "               ID in table. Please Enter New ID"
                                                userInput = ""
                                                # break

                                        if (userInput != ""):
                                            # if not in the table finds codename and prompts for machine code
                                            addedCodeName = str(key2)
                                            print("ID already exists, please input a new ID.") 
                                            addedID = str(key1)                          
                                            print(addedID)
                                            print(addedCodeName)
                                            idWords = "         ID found, please input a Machine Code."
                                            userInput = ""
                                            inputField = 2
                                            #print("Welcome back {codeName}")
                                            #supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute()  
                                            print("inside if statement " + " userInput = " + userInput + " key = " + str(key1))
                                    
                                elif ((userInput != str(key)) and (userInput != "") and (inputField == 0)):                           
                                    print("Welcome to the battlefield, enter your codename.")
                                    idWords = "Please Enter Code Name. Press Enter Key to Submit"
                                    
                                    if ((userInput != "") and (inputField == 0)):
                                        addPlayer = supabase.table('player').insert({ 'id': userInput}).execute()
                                        inputField = 1
                                        #set the addedID equal to the userInput
                                        addedID = userInput
                                        userInput = ""
                                    elif ((userInput != "") and (inputField == 1)):
                                        supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute() 

                            if (inputField == 1) and (userInput != ""):
                                supabase.table('player').update({ 'codename': userInput}).eq('id', addedID).execute()
                                fetchCodeName = supabase.table('player').select("codename").eq('id', addedID).execute()
                                print(fetchCodeName)
                                addedCodeName = userInput
                                inputField = 2
                                idWords = "Please Enter Machine Code. Press Enter Key to Submit"
                                userInput = ""
                                numPlayers += 1
                                #data_to_be_displayed = supabase.table('player').select("id").eq('id', addedID).execute()
                                response = supabase.table('player').select("*").eq('id', addedID).execute()
                                print(numPlayers)
                                # Extract the data part of the response
                                data = response.data

                                #Assuming there's at least one result and you want the first one
                                if data:
                                    codename = data[0]['codename']
                                    id = data[0]['id']
                                    print(codename)
                                    print (id)
                                
                                else:
                                    print("No data found.")

                            if (inputField == 2) and (userInput == ""):
                                while(event.key != pygame.K_RETURN):
                                    if event.type == pygame.KEYUP:
                                        if event.key == pygame.K_BACKSPACE:
                                            userInput = userInput[:-1]
                                    if event.type == pygame.QUIT:
                                        exitProgram = True
                                        inEntryScreen = False
                                    if event.key == pygame.K_MINUS:
                                        RedTeam.redPlayers.clear()
                                        GreenTeam.greenPlayers.clear()
                                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                                        exitProgram = True
                                        inEntryScreen = False
                                    else:
                                        userInput += event.unicode

                            if (inputField == 2) and (userInput != ""):
                                rLength = len(RedTeam.redPlayers)
                                gLength = len(GreenTeam.greenPlayers)
                                for i in range(rLength):
                                    if(RedTeam.redPlayers[i].id == addedID):
                                        inputField = 0
                                        idWords = "Please Enter Player ID. Press Enter Key to Submit"
                                        userInput = ""
                                        
                                        # break
                                for k in range(gLength):
                                    if(GreenTeam.greenPlayers[k].id == addedID):
                                        inputField = 0
                                        idWords = "Please Enter Player ID. Press Enter Key to Submit"
                                        userInput = ""
                                        
                                        # break
                                if (inputField != 0):
                                    listNotEmpty = True
                                    if (int(userInput) % 2 != 0):
                                        newPlayer = RedTeam(addedID, addedCodeName, userInput)
                                        RedTeam.redPlayers.append(newPlayer)
                                    if (int(userInput) % 2 == 0):
                                        newPlayer = GreenTeam(addedID, addedCodeName, userInput)
                                        GreenTeam.greenPlayers.append(newPlayer)
                                    userInput = "Hardware/" + userInput + "/" + addedID
                                    
                                    send_udp_packet(userInput)
                                    idWords = "Please Enter Player ID. Press Enter Key to Submit"
                                    inputField = 0
                                    userInput = ""        

            if active:
                InputBoxColor = InputColorActive
            else:
                InputBoxColor = InputColorPassive
            idText = inputBoxFont.render(idWords, True, YELLOW) # Input Box Message
            screen.blit(idText,(screen.get_width()/2 - screen.get_width()/3, screen.get_height()/2 +275))
            deleteStartText = inputBoxFont.render("'-' To Clear the Players '+' To Start Game", True, WHITE)
            screen.blit(deleteStartText,(screen.get_width()/2 - screen.get_width()/3.5, screen.get_height()/2 +250))
            redText = inputBoxFont.render("Red Team", True, RED) # Red Team
            screen.blit(redText,(screen.get_width()/4 - screen.get_width()/18, 12))
            redText = inputBoxFont.render("Green Team", True, GREEN) # Green Team
            screen.blit(redText,(screen.get_width() - screen.get_width()/4 - screen.get_width()/14, 12))
            pygame.draw.rect(screen, InputBoxColor, inputBox)
            textSurface = coolFont.render(userInput, True, YELLOW)
            screen.blit(textSurface, (inputBox.x+5, inputBox.y+5))
            inputBox.w = max(screen.get_width()/2, textSurface.get_width()+10)
            pygame.display.update()      
        pygame.display.flip()

        clock.tick(60)



def blit_text(surface, text, pos, font, color=pygame.Color('yellow')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


def main():
    print("Hello World")
    setup()
    
    


        
if __name__ == "__main__":
    main()




#PHOTON
#In a world where lasers (which aren't actually lasers but simpler infrared lights emitted as beams) KILL. 
#But they don't kill you, more like they kill your frabricated health assigned to your player when you signed up for this game. 
#EMBARK on a glorious journey of action, adventure, and space lasers. May your aim be true, good luck soldier.
