import random
import time
import pygame
import os
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 36)
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

currentDir = os.getcwd()
image_path = "frontend/logo.jpg"
full_path = os.path.join(currentDir,image_path) 

pygame.display.set_caption("Photon")
title = pygame.image.load(full_path).convert()
title = pygame.transform.scale(title, (500,400))
    
y = 0
i = 1


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
              
    screen.blit(title,(screen.get_width()/2 - title.get_width()/2,screen.get_height() - y))
    y = y + 1
    storytext = font.render("Welcome to Laser Tag", True, YELLOW)
    screen.blit(storytext,(screen.get_width()/2 - storytext.get_width()/2,screen.get_height() + title.get_height() -y))
    pygame.display.flip()

    clock.tick(60)


    end = time.time()
    total = end - start
    if (total > 20):
            done = True


def main():
    print("Hello World")

        
if __name__ == "__main__":
    main()




#PHOTON
#In a world where lasers (which aren't actually lasers but simpler infrared lights emitted as beams) KILL. 
#But they don't kill you, more like they kill your frabricated health assigned to your player when you signed up for this game. 
#EMBARK on a glorious journey of action, adventure, and space lasers. May your aim be true, good luck soldier.
