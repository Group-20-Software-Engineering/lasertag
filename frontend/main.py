import random
import pygame
#pygame.init()
def main():
    print("Hello World")
    WHITE = (255, 255, 255)
    done = False
    clock = pygame.time.Clock()
    while not done:
        size = (500,500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Photon")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        pygame.display.flip()

        clock.tick(60)
        
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