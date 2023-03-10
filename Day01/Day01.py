# Advent of Code 2022 Day 01
# Baillie Noell
# March 9th 2023

calories = 0
elves = []

input = open("Day01.txt", "r")

for line in input:
    if line.strip():
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0

input.close()

# Part 1
print("The max calories is ", max(elves))
print("The elf with the most calories is elf ", elves.index(max(elves))+1)

# Part 2
topThreeCalories = 0

for elf in range(3):
    topThreeCalories += max(elves)
    elves.remove(max(elves))

print("The total calories of the max 3 elves is ", topThreeCalories)
