left = []
right = []
similarity = 0

with open('input1.txt', 'r') as file:
    for line in file:
        num1, num2 = line.split()
        left.append(int(num1))
        right.append(int(num2))

for num in left:
    count = 0
    for num2 in right:
        if num == num2:
            count += 1
    similarity += num * count

print(similarity)