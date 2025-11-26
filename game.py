import random

class Player:
    def __init__(self, name=input()):
        self.name = name
        self.health = 100
        self.coin = 0
        self.x = 0
        self.y = 0
    
    def move(self, direction, map_size):
        if direction == 'w' and self.x > 0:
            self.x -= 1
        elif direction == 's' and self.x < map_size - 1:
            self.x += 1
        elif direction == 'a' and self.y > 0:
            self.y -= 1
        elif direction == 'd' and self.y < map_size - 1:
            self.y += 1
        else:
            print("You cannot move that way!")

class GameMap:
    def __init__(self, size=9):
        self.size = size
    
    def draw(self, player):
        for i in range(self.size):
            for j in range(self.size):
                if i == player.x and j == player.y:
                    print("C", end = "  ")
                elif i == self.size - 1 and j == self.size - 1:
                    print("M", end = "  ")
                else:
                    print(".", end = "  ")
            print()
        print()
        print(f"Health: {player.health}")
        print("-------------------------")
        print(f"Coin: {player.coin}")
        print("=========================")

class Game:
    def __init__(self):
        self.player = Player()
        self.map = GameMap()
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.map_size = self.map.size
    
    def check_event(self):
        event = random.choice(self.events)
        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10
    
    def play(self):
        self.map.draw(self.player)
        direction = input("Your next move (w/a/s/d/q):")
        while direction != 'q':
            self.player.move(direction, self.map.size)
            if self.player.x == self.map.size - 1 and self.player.y == self.map.size -1:
                print("Congratulations! You reached the monster and won the game!")
                break
            self.check_event()
            self.map.draw(self.player)
            direction = input("Your next move (w/a/s/d/q):")

if __name__ == '__main__':
    Game().play()