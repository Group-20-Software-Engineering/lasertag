import sys
import random
import time
import pygame
import textwrap
import os
from send import send_udp_packet

#supabase api stuff
from supabase import create_client, Client 
url: str = "https://jmfukmeanfezxzgrsitj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptZnVrbWVhbmZlenh6Z3JzaXRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNTEyMDMsImV4cCI6MjAyMjgyNzIwM30.r99dqev77H1YPfAudZ9xm5heBt-jR-dNDiuI8-xVuZk"
supabase: Client = create_client(url, key)

pygame.init()
pygame.key.set_repeat(500, 100)

currentDir = os.getcwd()

#coolFontName = os.path.join(currentDir, "frontend/8-bit.ttf")
coolFontName = "8-bit.ttf"
defFontName = "freesansbold.ttf"
coolFont = pygame.font.Font(coolFontName, 18) #changing font because on mine it doesn't work for the cool font
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
idNamePairFound = True
clock = pygame.time.Clock()
size = (900,700)
screen = pygame.display.set_mode(size)
# story = """In a world where lasers
#         (which aren't actually lasers
#         but simpler infrared lights
#         emitted as beams)
#                 KILL.
                
#             But they don't kill you,
#         more like they kill your
#         frabricated health assigned
#         to your player when
#         you signed up for
#         this game.

#             EMBARK on a glorious 
#         journey of action, adventure, 
#         and space lasers.

#             May your aim be true,
#         good luck soldier."""    


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



image_path = "logo.jpg"

center = screen.get_rect().center

pygame.display.set_caption("Photon")
title = pygame.image.load(image_path).convert()
title = pygame.transform.scale(title, (500,242))
    
y = 0
i = 1
userInput = ''
InputColorActive = pygame.Color('lightskyblue3')
InputColorPassive = pygame.Color('chartreuse4')
InputBoxColor = InputColorPassive
active = False
inputBox = pygame.Rect(screen.get_width()/2 - screen.get_width()/4, screen.get_height()/2 + 300, screen.get_width()/2, 40)
start = time.time()


while not exitIntroScreen:
        
    #WHEN SENDING HARDWARE ID USE THE FORMAT "Hardware/ID" AS SEEN BELLOW
    test = "Hardware/9"
    send_udp_packet(test)

    screen.fill(BLACK)

    
    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)

    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)

    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)

    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)

    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)
    
    a = random.randrange(899) + 1
    b = random.randrange(699) + 1
    pygame.draw.circle(screen, WHITE,(a,b), 2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitProgram = True
        
     

      
    

    
    y = y + 1
    rocketText = "        !\n        !\n        ^\n      /    \\\n    /____\\\n    |=    =|\n    |        |\n    |        |\n    |        |\n    |        |\n    |        |\n   /|##!##|\\\n  / |##!##| \\\n /  |##!##|  \\\n |  / ^ | ^ \\  |\n | /   ( | )   \\ |\n |/    ( | )    \\|\n      ((   ))\n     ((  :  ))\n     ((  :  ))\n      ((   ))\n       (( ))\n        ( )\n         |\n         |\n         |\n         |\n"
    blit_text(screen, rocketText, (screen.get_width()/2 - title.get_width()/2 + 185, 25 - y), defFont)
    screen.blit(title,(screen.get_width()/2 - title.get_width()/2, screen.get_height() - y))
    storyText = "\n\n             In a world where lasers\n        (which aren't actually lasers\n         but simpler infrared lights\n                  emitted as beams)\n                           KILL.\n\n             But they don't kill you,\n            more like they kill your\n         fabricated health assigned\n             to your player when you\n            signed up for this game.\n\n              EMBARK on a glorious\n       journey of action, adventure,\n                  and space lasers.\n\n               May your aim be true,\n                 good luck soldier."
    # storyText = textwrap.dedent('''\n\n             
    #    In a world where lasers\n        
    #    (which aren't actually lasers\n         
    #    but simpler infrared lights\n                   
    #    emitted as beams)\n                            
    #    KILL.\n\n            
    #    But they don't kill you,\n           
    #    more like they kill your\n        
    #    fabricated health assigned\n            
    #    to your player when you\n           
    #    signed up for this game.\n\n              
    #    EMBARK on a glorious\n        
    #    journey of action, adventure,\n                  
    #    and space lasers.\n\n               
    #    May your aim be true,\n                 
    #   good luck soldier.''')
    blit_text(screen, storyText, (screen.get_width()/2 - title.get_width()/2 - 40,screen.get_height() + title.get_height() - y), coolFont)
    # storytext = coolFont.render("Welcome to Laser Tag", True, YELLOW)
    # screen.blit(storytext,(screen.get_width()/2 - storytext.get_width()/2,screen.get_height() + title.get_height() -y))
    
    end = time.time()
    total = end - start
    if (total > 1):
        exitIntroScreen = True
        inEntryScreen = True
    

    while ((exitIntroScreen == True) and (inEntryScreen == True)):
        screen.fill(BLACK)
        # left_rect = pygame.Rect(0, 0, screen.get_width()/2, 624)
        # pygame.draw.rect(screen, RED, left_rect)
        # right_rect = pygame.Rect(screen.get_width()/2, 0, screen.get_width()/2, 624)
        # pygame.draw.rect(screen, GREEN, right_rect)

        rect_width = 900/4
        rect_height = 580/16
        for row in range(16):
            for col in range(2):
                x = col * rect_width
                y = row * rect_height + 44
                rect = pygame.Rect(x, y, rect_width, rect_height)
                pygame.draw.rect(screen, BLACK, rect, 1)
                pygame.draw.rect(screen, RED, rect.inflate(-2, -2))

        for row in range(16):
            for col in range(2):
                x = col * rect_width + screen.get_width() / 2
                y = row * rect_height + 44
                rect = pygame.Rect(x, y, rect_width, rect_height)
                pygame.draw.rect(screen, BLACK, rect, 1)
                pygame.draw.rect(screen, GREEN, rect.inflate(-2, -2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitProgram = True
                inEntryScreen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userInput = userInput[:-1]
                    """
                    fetchId = supabase.table('player').select('id').eq('id', userInput).execute()
                    if not FetchId:
                        print("Welcome to the battlefield, enter your codename.")
                        addPlayer = supabase.table('player').insert({ 'id': userInput, 'codename': codeName }).execute()
                    else:
                        print("Welcome back {codeName}")
                    #put id and codename pair onto table    
                    """
                elif event.key == pygame.K_MINUS or event.key == pygame.K_ESCAPE:
                    inEntryScreen = False
                    exitProgram = True
                else:
                    if (event.key != pygame.K_RETURN):
                        userInput += event.unicode
                    else:
                        userInput = ""
                        #code to send userInput to the database

                        
            #if userInput == 'exists':
                #idNamePairFound = True
                #display welcome text with registered codename - potental option to change existing codename
                #ask for users machine code
                #start game button
                     
        if active:
            InputBoxColor = InputColorActive
        else:
            InputBoxColor = InputColorPassive
        idText = inputBoxFont.render("Please Enter Player ID. Press Enter Key to Submit", True, YELLOW) # Input Box Message
        screen.blit(idText,(screen.get_width()/2 - screen.get_width()/3, screen.get_height()/2 +275))
        redText = inputBoxFont.render("Red Team", True, RED) # Red Team
        screen.blit(redText,(screen.get_width()/4 - screen.get_width()/18, 12))
        redText = inputBoxFont.render("Green Team", True, GREEN) # Green Team
        screen.blit(redText,(screen.get_width() - screen.get_width()/4 - screen.get_width()/14, 12))
        pygame.draw.rect(screen, InputBoxColor, inputBox)
        textSurface = coolFont.render(userInput, True, YELLOW)
        screen.blit(textSurface, (inputBox.x+5, inputBox.y+5))
        inputBox.w = max(screen.get_width()/2, textSurface.get_width()+10)
        pygame.display.update()
        # random ass pseudocode blabber
        # if (idNamePairFound == True): go to next id selection
        # elif (idNamePairFound == False): do nameText instead of idText, "Name Not Found. Please Enter Player Name", prompt again, pair it up
        # have a button underneath to start game, activates next part inPlayerScoreboard, have two tables of teams and scores and shit
        # at end have exitProgram = True
    pygame.display.flip()

    clock.tick(60)

def main():
    print("Hello World")
    


        
if __name__ == "__main__":
    main()




#PHOTON
#In a world where lasers (which aren't actually lasers but simpler infrared lights emitted as beams) KILL. 
#But they don't kill you, more like they kill your frabricated health assigned to your player when you signed up for this game. 
#EMBARK on a glorious journey of action, adventure, and space lasers. May your aim be true, good luck soldier.
