import random
import pygame
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 36)
WHITE = (255, 255, 255)
BLUE = (0, 71, 171)
done = False
clock = pygame.time.Clock()
size = (900,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Photon")
title = pygame.image.load("C:\\Users\\zheng\\OneDrive\\Desktop\\software\\lasertag\\frontend\\logo.jpg").convert()
title = pygame.transform.scale(title, (500,400))
    
y = 0
  
while not done:
        
        
        
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
              
    screen.blit(title,(screen.get_width()/2 - title.get_width()/2,screen.get_height() - y))
    y = y + 1
    storytext = font.render("Hello World", True, WHITE)
    screen.blit(storytext,(screen.get_width()/2 - storytext.get_width()/2,screen.get_height() + title.get_height() -y))
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



class Player:
    def __init__(self, name):   #self is a reference to the current instance of the class -- self = this in java
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class LaserTagGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        print("Player 1: {} (Health: {})".format(self.player1.name, self.player1.health))
        print("Player 2: {} (Health: {})".format(self.player2.name, self.player2.health))

        damage = random.randint(10, 20)
        print("Player 1 shoots Player 2 and deals {} damage!".format(damage))
        self.player2.take_damage(damage)

        damage = random.randint(10, 20)
        print("Player 2 shoots Player 1 and deals {} damage!".format(damage))
        self.player1.take_damage(damage)

    def run_game(self):
        round_num = 1
        while self.player1.is_alive() and self.player2.is_alive():
            print("Round", round_num)
            self.play_round()
            round_num += 1

        if self.player1.is_alive():
            print(self.player1.name, "wins!")
        else:
            print(self.player2.name, "wins!")

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Start the game
game = LaserTagGame(player1, player2)
game.run_game()