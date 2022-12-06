
def read_file(path):
    file = open(path, "r")
    lines = file.readlines()

    box_lines = []
    move_lines = []

    for line in lines:
        if "[" in line:
            box_lines.append(line)
        elif "move" in line:
            move_lines.append(line)
            
    return box_lines, move_lines

def split_line(line):

    boxes = []
    for i in range(int(len(line) / 4)):
        boxes.append(line[i*4:i*4+4])

    return boxes

def add_to_col(lines):
    boxes = []
    height = 0
    width = 0
    skip = 0

    for line in lines:
        box_row = split_line(line)

        for box in box_row:

                
            if box.strip() != "":
                try:
                    boxes[width].append(box_row[width].strip()[1]) #[1] to get 'M' from [M]
                except:
                    boxes.append([box_row[width].strip()[1]])
            else:
                skip += 1

            width += 1
            if width >= len(box_row):
                width = 0
                height += 1

    return boxes
        
def get_instructions(lines):
    instruction_set = []

    for line in lines:
        line_split = line.strip().split(" ")
        amount = int(line_split[1].strip())
        src = int(line_split[3].strip())
        dest = int(line_split[5].strip())

        instruction_set.append([amount, src, dest])

    return instruction_set

def move(boxes, moves):
    for move in moves:
        amount = move[0]
        src = move[1] -1
        dest = move[2] -1

        temp_arr = []
        for i in range(amount):
            temp_arr.append(boxes[src].pop())
        temp_arr.reverse()
        boxes[dest] = [*boxes[dest], *temp_arr]

    result = ""
    for stack in boxes:
        result += stack[-1]
    print("result: ", result)

box_lines, move_lines = read_file("input.txt")
box_lines.reverse()
boxes = add_to_col(box_lines)
moves = get_instructions(move_lines)
move(boxes, moves)