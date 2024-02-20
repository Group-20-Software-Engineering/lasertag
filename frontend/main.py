import random
import time
import pygame
import os


pygame.init()

currentDir = os.getcwd()

#coolFontName = os.path.join(currentDir, "frontend/8-bit.ttf")
coolFontName = "8-bit.ttf"
defFontName = "freesansbold.ttf"
coolFont = pygame.font.Font(coolFontName, 18) #changing font because on mine it doesn't work for the cool font
defFont = pygame.font.Font(defFontName, 24)
WHITE = (255, 255, 255)
BLUE = (0, 71, 171)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
done = False
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
inputBox = pygame.Rect(200, 200, 140, 32)
start = time.time()


while not done:
        
        
        
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
            done = True
        
     

      
    

    
    y = y + 1
    rocketText = "        !\n        !\n        ^\n      /    \\\n    /____\\\n    |=    =|\n    |        |\n    |        |\n    |        |\n    |        |\n    |        |\n   /|##!##|\\\n  / |##!##| \\\n /  |##!##|  \\\n |  / ^ | ^ \\  |\n | /   ( | )   \\ |\n |/    ( | )    \\|\n      ((   ))\n     ((  :  ))\n     ((  :  ))\n      ((   ))\n       (( ))\n        ( )\n         |\n         |\n         |\n         |\n"
    blit_text(screen, rocketText, (screen.get_width()/2 - title.get_width()/2 + 185, 20 - y), defFont)
    screen.blit(title,(screen.get_width()/2 - title.get_width()/2,screen.get_height() - y))
    storyText = "\n\n             In a world where lasers\n        (which aren't actually lasers\n         but simpler infrared lights\n                   emitted as beams)\n                            KILL.\n\n            But they don't kill you,\n           more like they kill your\n        fabricated health assigned\n            to your player when you\n           signed up for this game.\n\n              EMBARK on a glorious\n        journey of action, adventure,\n                  and space lasers.\n\n               May your aim be true,\n                 good luck soldier."
    blit_text(screen, storyText, (screen.get_width()/2 - title.get_width()/2 - 40,screen.get_height() + title.get_height() - y), coolFont)
    # storytext = coolFont.render("Welcome to Laser Tag", True, YELLOW)
    # screen.blit(storytext,(screen.get_width()/2 - storytext.get_width()/2,screen.get_height() + title.get_height() -y))
    
    
    end = time.time()
    total = end - start
    if (total > 2):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userInput = userInput[:-1]
                else:
                    userInput += event.unicode
        if active:
            InputBoxColor = InputColorActive
        else:
            InputBoxColor = InputColorPassive
        pygame.draw.rect(screen, InputBoxColor, inputBox)
        textSurface = coolFont.render(userInput, True, (255, 255, 255))
        screen.blit(textSurface, (inputBox.x+5, inputBox.y+5))
        inputBox.w = max(100, textSurface.get_width()+10)
        #done = True
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
