# Advent of Code 2022 Day 3
# Baillie Noell
# March 9th 2023

from itertools import islice
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

print("The sum of the part 1 priorities is ", sum)

# Part 2
sum = 0

rucksacks = open("Day03_Input.txt")

while True:
    sack1 = rucksacks.readline().strip()
    sack2 = rucksacks.readline().strip()
    sack3 = rucksacks.readline().strip()

    if not sack1:
        break

    for b in sack1:
        if b in sack2 and b in sack3:
            sum += priorities.find(b)
            break

rucksacks.close()

print ("The sum of the part 2 priorities is ", sum)
