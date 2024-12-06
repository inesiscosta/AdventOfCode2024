""" Day 1: Part 2 of Advent of Code 2024 """
left = []
right = []
SIMILARITY = 0

with open('day1_input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        num1, num2 = line.split()
        left.append(int(num1))
        right.append(int(num2))

for num in left:
    COUNT = 0
    for num2 in right:
        if num == num2:
            COUNT += 1
    SIMILARITY += num * COUNT

print(SIMILARITY)
