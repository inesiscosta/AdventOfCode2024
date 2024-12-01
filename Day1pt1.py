left = []
right = []
sum_ranges = 0

with open('input1.txt', 'r') as file:
    for line in file:
        num1, num2 = line.split()
        left.append(int(num1))
        right.append(int(num2))

left.sort()
right.sort()

for i in range(len(left)):
    sum_ranges += (abs(left[i] - right[i]))

print(sum_ranges)
