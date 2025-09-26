import random


game_name = "Escaping"
print(f"Welcome to {game_name}!")  # TODO, print greetings with game name
print("====================") # TODO, add or remove equal symbol to align the greetings

# Ask for the character's name
name = input("Before we begin, what is your character's name?\n> ")

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

player = {
    "Name": name,
    "Health": 100,
    "Coin": 0
}

events = ["find a coin", "meet a monster", "do nothing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player["Coin"] = player["Coin"] + 1
    print(f'{player["Name"]} found a coin, {player["Name"]} has {player["Coin"]} coins.')

elif event == "meet a monster":
    player["Health"] = player["Health"] - 10
    print(f"{player["Name"]} got hurt during the combat with monster, health is now {player["Health"]}.")