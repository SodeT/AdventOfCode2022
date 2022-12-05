import numpy as np


def read_input(file):
    instructions = False
    boxes = []
    lines = file.readlines()

    width = 0
    height = 0

    for line in lines:
        if line.strip()[0] == "1":
            boxes = [[0 for col in range(width)] for row in range(height)]
            break

        width = int(len(line)/4)
        height += 1


    current_depth = 0
    for line in lines:

        if  line.strip() == "":
            instructions = True
            pass_now = True

        elif line.strip()[0] == "1":
            instructions = True
            pass_now = True

        if instructions == False:
            for i in range(width):
                boxes[i][current_depth] = line[i*4:i*4+4].strip()
            
            current_depth += 1


        if instructions:
            if pass_now == False:
                line_arr = line.split(" ")
                print(line_arr)
                print(line_arr[1])
                move_count = int(str(line_arr[1]).strip())
                source = int(line_arr[5].strip()) -1
                dest = int(line_arr[3].strip()) -1

                print("mv src dest: ", move_count, source, dest)
                boxes[dest].insert(0, boxes[source].pop(0))
                print("box: ", boxes)
            else:
                pass_now = False
                for x in range(len(boxes)):
                    for y in range(len(boxes[x])):
                        if boxes[x][y] == "":
                            boxes[x].pop(y)
    return boxes

file = open("input.txt", "r")
print("end: ", read_input(file))
