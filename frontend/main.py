import random
import pygame
#pygame.init()
def main():
    print("Hello World")
    while(1==1):
        size = (500,500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Photon")
if __name__ == "__main__":
    main()
#write a python front end for a laser tag game using the pygame library
#this is the main file that will be run to start the game
#this file will be responsible for setting up the game and running the game loop
#this file will also be responsible for handling user input and updating the game state
#this file will also be responsible for rendering the game state to the screen
#this file will also be responsible for handling game events such as collisions and scoring
#this file will also be responsible for handling game over conditions and ending the game
#this file will also be responsible for handling game restarts and resets
#this file will also be responsible for handling game exits and closing the game window
#this file will also be responsible for handling game settings and options
#this file will also be responsible for handling game audio and sound effects
#this file will also be responsible for handling game graphics and visual effects
#this file will also be responsible for handling game networking and multiplayer
#this file will also be responsible for handling game saving and loading




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