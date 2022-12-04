
def checklines(file):
    
    lines = file.readlines()

    overlaps = 0

    for line in lines:
        line = line.strip()

        elf = line.split(",")
        elf1_1, elf1_2 = elf[0].split("-")
        elf2_1, elf2_2 = elf[1].split("-")


        if int(elf1_1) <= int(elf2_1) and int(elf1_2) >= int(elf2_2):
            overlaps += 1

        elif int(elf1_1) >= int(elf2_1) and int(elf1_2) <= int(elf2_2):
            overlaps += 1 
    
    return overlaps

file = open("input.txt", "r")
print(checklines(file))
