
chars = ""
file = open("input.txt", "r")
file = file.readlines()[0]

for i in range(len(str(file))):
    chars = file[i-4:i]
    if chars.strip() == "":
        continue    

    if len(set(chars)) == len(chars):
        print(i)
        break