import sys
import random
import time
import pygame
import textwrap

import os
from send import send_udp_packet

from supabase import create_client, Client 

url: str = "https://jmfukmeanfezxzgrsitj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptZnVrbWVhbmZlenh6Z3JzaXRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNTEyMDMsImV4cCI6MjAyMjgyNzIwM30.r99dqev77H1YPfAudZ9xm5heBt-jR-dNDiuI8-xVuZk"

supabase: Client = create_client(url, key)

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
countDownBox = pygame.Rect(screen.get_width()/2 - screen.get_width()/17, screen.get_height()/40,100,40)
done = False
while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    redText = DisplayBoxFont.render("Red Team", True, RED) # Red Team
    screen.blit(redText,(screen.get_width()/4 - screen.get_width()/18, 12))
    greenText = DisplayBoxFont.render("Green Team", True, GREEN) # Green Team
    screen.blit(greenText,(screen.get_width() - screen.get_width()/4 - screen.get_width()/14, 12))
    pygame.draw.rect(screen, BLUE, countDownBox)
    pygame.display.flip()
    clock.tick(60)

def main():
    print("Hello World")
    


        
if __name__ == "__main__":
    main()