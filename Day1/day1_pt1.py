""" Day 1: Part 1 of Advent of Code 2024 """
left = []
right = []
SUM_RANGES = 0

with open('day1_input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        num1, num2 = line.split()
        left.append(int(num1))
        right.append(int(num2))

left.sort()
right.sort()

for l, r in zip(left, right):
    SUM_RANGES += abs(l - r)

print(SUM_RANGES)
