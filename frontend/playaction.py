import sys
import random
import time
import pygame
import textwrap

import os
from send import send_udp_packet

pygame.init()
pygame.key.set_repeat(500, 100)
coolFontName = "8-bit.ttf"
defFontName = "freesansbold.ttf"
coolFont = pygame.font.Font(coolFontName, 18)
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

timer30sec = 0
timer6min = 1
timerState = timer30sec
totalTime = 30
startTime = pygame.time.get_ticks()

while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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
    timer = coolFont.render(timeText, True, WHITE)
    countDownBoxRect = timer.get_rect(center=countDownBox.center)
    screen.blit(timer, countDownBoxRect)
    rect = pygame.Rect(0, 75, 448, 300)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    rect = pygame.Rect(screen.get_width() / 2 + 2, 75, 448, 300)
    pygame.draw.rect(screen, GREEN, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    rect = pygame.Rect(0, 378, 900, 320)
    pygame.draw.rect(screen, BLUE, rect, 1)
    pygame.draw.rect(screen, BLACK, rect.inflate(-2, -2))
    pygame.display.flip()
    clock.tick(60)

def main():
    print("Hello World")
    


        
if __name__ == "__main__":
    main()