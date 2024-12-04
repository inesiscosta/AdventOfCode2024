""" Day 4: Part 1 of Advent of Code 2024 """
rows = []
# Read the input file and store each line as a list of characters in 'rows'
with open('day4_input.txt', encoding='utf8') as file:
    rows = [list(line.strip()) for line in file]

WORD = "XMAS"  # The word we are searching for
WORD_COUNT = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i, row in enumerate(rows):
    for j, character in enumerate(row):
        if character == WORD[0]:
            # Check all 8 possible directions
            for dx, dy in directions:
                # Check if the word can be formed in the current direction
                if all(0 <= i + k * dx < len(rows) and 0 <= j + k * dy < len(row) and rows[i + k * dx][j + k * dy] == WORD[k] for k in range(len(WORD))):
                    WORD_COUNT += 1

print(WORD_COUNT)
