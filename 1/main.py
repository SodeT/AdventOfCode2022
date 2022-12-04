
def split(input):
    lines = input.readlines()

    elfes = []
    calories = 0

    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()

        if len(line) == 0:
            elfes.append(calories)
            calories = 0
        else:
            calories += int(line)

    return elfes

input = open("input.txt", "r")

elfes = sorted(split(input))

elfes = list(reversed(elfes))

top_3 = 0
for i in range(3):
    top_3 += elfes[i]

print(top_3)

