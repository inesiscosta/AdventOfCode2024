""" Day 3: Part 1 of Advent of Code 2024 """
import re

with open("day3_input.txt", 'r', encoding='utf-8') as file:
    data = file.read()

TOTAL = 0
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)

for match in matches:
    num1, num2 = map(int, match)
    TOTAL += num1 * num2

print(TOTAL)
