""" Day 3: Part 2 of Advent of Code 2024 """
import re

with open("day3_input.txt", 'r', encoding='utf-8') as file:
    data = [line.split("don't()")[0].strip() for line in file.read().split("do()")]

TOTAL = 0

for element in data:
    matches = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)').findall(element)
    for match in matches:
        num1, num2 = map(int, match)
        TOTAL += num1 * num2

print(TOTAL)
