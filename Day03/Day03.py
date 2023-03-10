# Advent of Code 2022 Day 3
# Baillie Noell
# March 9th 2023

sum = 0
priorities = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
rucksacks = open("Day03_Input.txt")

for sack in rucksacks:
    sack = sack.strip()
    c1 = []
    c2 = []
    length = len(sack)

    for c in range(int(length/2)):
        c1.append(sack[c])
    for c in range(int(length/2), length):
        c2.append(sack[c])

    for c in c1:
        if c in c2:
            sum += priorities.find(c)
            break

rucksacks.close() 

print("The sum of the priorities is ", sum)
