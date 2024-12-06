""" Day 4: Part 2 of Advent of Code 2024 """
with open('day4_input.txt', encoding='utf8') as file:
    rows = [list(line.strip()) for line in file]

WORD = "MAS" # The word we are searching for
CROSS_COUNT = 0
directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
MIDDLE_INDEX = len(WORD) // 2

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char == WORD[MIDDLE_INDEX]:
            WORD_COUNT = 0
            for dx, dy in directions:
                if all(0 <= i + dx * (k - MIDDLE_INDEX) < len(rows) and 0 <= j + dy * (k - MIDDLE_INDEX) < len(row) and rows[i + dx * (k - MIDDLE_INDEX)][j + dy * (k - MIDDLE_INDEX)] == WORD[k] for k in range(len(WORD))):
                    WORD_COUNT += 1
            if WORD_COUNT >= 2:
                CROSS_COUNT += 1

print(CROSS_COUNT)
