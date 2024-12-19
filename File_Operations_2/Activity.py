# using with function write some texts in the file
with open("file.txt","w") as file:
    file.write("Hi I am Munawwar and I love traveling")

file.close()

with open("file.txt","r") as file:
    data = file.readlines()
    print("Words in the file are:")
    for line in data:
        word = line.split()
        print(word)

file.close()