
class folder_class:
    size = 0
    name = ""
    nested_folders = []
    files = []
    total_size = 0
    size_checked = False

def read_input(lines):

    folders = []

    dir = folder_class()
    ls_ret = False
    for line in lines:

        if "$ cd .." in line:
            for folder in folders:
                if dir.name in folder.nested_folders:
                    dir = folder

        elif "$ cd" in line:
            ls_ret = False
            folders.append(dir)
            dir = folder_class()
            dir.name = line[4:].strip()

        elif "$ ls" in line:
            ls_ret = True
        
        elif ls_ret:
            if "dir" in line:
                dir.nested_folders.append(line.split(" ")[1].strip())
                print(dir.nested_folders[-1])
            elif line.split(" ")[0].isnumeric():
                dir.files.append([int(line.split(" ")[0].strip()), line.split(" ")[1].strip()])

    return folders

def file_sizes(folders):

    for folder in folders:
        for file in folder.files:
            folder.total_size += file[0] # file = [size, "name"]

    return folders

def get_size(folder, folders):
    folders_to_check = []

    for ftc in folder.nested_folders:
        ret = get_folder(ftc, folders)
        if ret != 0:
            folders_to_check.append(ret)
        else:
            pass #print("error: ", ftc)

    folders_checked = []

    not_checked = []

    for ftc in folders_to_check:
        folder.total_size += ftc.total_size
        not_checked.append(ftc)            

    while len(not_checked) > 0:
        res, not_checked = check_nested(not_checked, folders)
        folder.total_size += res


    return folder
    
def check_nested(not_checked, folders):
    new_not_checked = []
    total = 0
    for nc in not_checked:
        for nested_folder_name in nc.nested_folders:
            print(nested_folder_name)
            nested_folder = get_folder(nested_folder_name, folders)
            total += nested_folder.total_size
            if len(nested_folder.nested_folders) > 0:
                new_not_checked.append(list(nested_folder.nested_folders))
    return total, new_not_checked



def get_folder(name, folders):
    for folder in folders:
        print("\"" + folder.name.strip() + "\" : ", name)
        if folder.name == name:
            print("true")
            return folders[folders.index(folder)]


    return 0

file = open("input.txt", "r")
lines = file.readlines()
folders = read_input(lines)
folders = file_sizes(folders)

arr = []


for folder in folders:
    arr.append(get_size(folder, folders))

for e in arr:
    if e.total_size > 10000:
        arr.pop(arr.index(e))
largest = 0
for e in arr:
    if e.total_size > largest:
        largest = e.total_size

print(largest)