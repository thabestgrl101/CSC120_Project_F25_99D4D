import random


game_name = "Escaping"
print(f"Welcome to {game_name}!")  # TODO, print greetings with game name
print("=========================") # TODO, add or remove equal symbol to align the greetings

# Ask for the character's name
name = "Tester"

player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

events = ["find a coin", "meet a monster", "do nothing"]

map_size = 9

def check_event():
    global events, player
    event = random.choice(events)


    if event == "find a coin":
        player["coin"] = player["coin"] + 1
    

    elif event == "meet a monster":
        player["health"] = player["health"] - 10

def draw_ui(x, y):
    for i in range(map_size):
        for j in range(map_size):
            if i == x and j == y:
                print("C", end = "  ") # two spaces
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end = "  ")
            else:
                print(".", end = "  ")
        print()
    print()
    print(f"health: {player['health']}")
    print("-------------------------")
    print(f"coin: {player["coin"]}")
    print("=========================")

def move(direction):
    if direction == 'w' and player['y'] > 0:
        player["y"] -= 1
    elif direction == 's' and player['x'] < map_size - 1:
        player["x"] += 1
    elif direction == 'a' and player['x'] > 0:
        player["x"] -= 1
    elif direction == 'd' and player['y'] < map_size - 1:
        player["y"] += 1
    else:
        print("You cannot move that way!")

def main():
    draw_ui(0, 0)
    direction = input("Your next move (w/a/s/d/q)")
    while direction != 'q':
        move(direction)
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        check_event()

        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q)")

if __name__ == '__main__':
    main()