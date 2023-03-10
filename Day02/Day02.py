# Advent of Code 2022 Day 02
# Baillie Noell
# March 9th 2023

# Part 1
points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "W": 6,
    "D": 3,
    "L": 0
}

ties = {
    "A": "X",
    "B": "Y",
    "C": "Z" 
}

wins = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

score = 0

games = open("Day02_Input.txt")

for game in games:
    score += points[game[2]]
    if game[2] == ties[game[0]]:
        score += points["D"]
    elif game[2] == wins[game[0]]:
        score += points["L"]
    else:
        score += points["W"]

games.close()

print("The total score for part 1 is ", score)


# Part 2
points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
    "R": 1,
    "P": 2,
    "S": 3
}

ties = {
    "A": "R",
    "B": "P",
    "C": "S" 
}

losses = {
    "A": "S",
    "B": "R",
    "C": "P"
}

wins = {
    "A": "P",
    "B": "S",
    "C": "R"
}

score = 0

games = open("Day02_Input.txt")

for game in games:
    score += points[game[2]]
    if game[2] == "X":
        score += points[losses[game[0]]]
    elif game[2] == "Y":
        score += points[ties[game[0]]]
    elif game[2] == "Z":
        score += points[wins[game[0]]]

games.close()

print("The total score for part 2 is ", score)