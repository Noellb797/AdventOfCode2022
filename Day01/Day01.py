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

print("The max calories is ", max(elves))
print("The elf with the most calories is elf ", elves.index(max(elves))+1)
