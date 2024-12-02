""" Day 2: Part 1 of Advent of Code 2024 """
with open('input2.txt', 'r', encoding='utf-8') as file:
    lines = [[int(number) for number in line.split()] for line in file]

SAFE = 0
for line in lines:
    ASCENDING = True
    DESCENDING = True
    for i in range(1, len(line)):
        if not 1 <= line[i] - line[i-1] <= 3:
            ASCENDING = False
        if not 1 <= line[i-1] - line[i] <= 3:
            DESCENDING = False
        elif not(ASCENDING or DESCENDING):
            break
    if ASCENDING or DESCENDING:
        SAFE += 1
print(SAFE)
