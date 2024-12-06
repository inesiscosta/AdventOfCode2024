""" Day 5: Part 1 of Advent of Code 2024 """
with open('day5_input.txt', 'r', encoding='utf8') as file:
    rules_str, updates_str = file.read().strip().split('\n\n')

rules = [(int(rule.split('|')[0]), int(rule.split('|')[1])) for rule in rules_str.split('\n')]
updates = [list(map(int, update.split(','))) for update in updates_str.split('\n')]

correct_updates = []

for update in updates:
    if all(update.index(x) < update.index(y) for x, y in rules if x in update and y in update):
        correct_updates.append(update)

middle_pages_sum = sum(update[len(update) // 2] for update in correct_updates)

print(middle_pages_sum)
