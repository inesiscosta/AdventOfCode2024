#pylint: skip-file
""" Day 5: Part 2 of Advent of Code 2024 """

def parse_input(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        rules_str, updates_str = file.read().strip().split('\n\n')
    rules = [(int(rule.split('|')[0]), int(rule.split('|')[1])) for rule in rules_str.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates_str.split('\n')]
    return rules, updates

def find_incorrect_updates(rules, updates):
    incorrect_updates = []
    for update in updates:
        if not all(update.index(x) < update.index(y) for x, y in rules if x in update and y in update):
            incorrect_updates.append(update)
    return incorrect_updates

def fix_updates(rules, incorrect_updates):
    fixed_updates = []
    for update in incorrect_updates:
        sorted_update = sorted(update, key=lambda x: [-1 if (x, y) in rules else 1 if (y, x) in rules else 0 for y in update])
        fixed_updates.append(sorted_update)
    return fixed_updates

def sum_middle_numbers(fixed_updates):
    middle_numbers = [update[len(update) // 2] for update in fixed_updates]
    return sum(middle_numbers)

def main():
    rules, updates = parse_input('day5_input.txt')
    incorrect_updates = find_incorrect_updates(rules, updates)
    fixed_updates = fix_updates(rules, incorrect_updates)
    total = sum_middle_numbers(fixed_updates)
    print(total)

if __name__ == "__main__":
    main()
