
def checklines(file):
    
    lines = file.readlines()

    overlaps = 0

    for line in lines:
        line = line.strip()

        elf = line.split(",")
        
        elf1_1, elf1_2 = elf[0].split("-")
        
        elf1 = range(int(elf1_1), int(elf1_2) +1)

        elf2_1, elf2_2 = elf[1].split("-")
        elf2 = range(int(elf2_1), int(elf2_2) +1)

        for sec1 in elf1:
            if sec1 in elf2:
                overlaps += 1
                break

    
    return overlaps

file = open("input.txt", "r")
print(checklines(file))
