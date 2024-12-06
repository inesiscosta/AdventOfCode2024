""" Day 2: Part 2 of Advent of Code 2024 """
with open('day2_input.txt', 'r', encoding='utf-8') as file:
    lines = [[int(number) for number in line.split()] for line in file]

SAFE = 0

for line in lines:
    sublines = [line[:i] + line[i+1:] for i in range(len(line))]
    sublines.append(line)
    for subline in sublines:
        ASCENDING = True
        DESCENDING = True
        for i in range(1, len(subline)):
            if not 1 <= subline[i] - subline[i-1] <= 3:
                ASCENDING = False
            if not 1 <= subline[i-1] - subline[i] <= 3:
                DESCENDING = False
        if ASCENDING or DESCENDING:
            SAFE += 1
            break

print(SAFE)
