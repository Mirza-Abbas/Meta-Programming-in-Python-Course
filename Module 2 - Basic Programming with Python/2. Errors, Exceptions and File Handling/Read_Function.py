print("Reading all content: \n")
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

print("Reading Specific Characters: \n")
with open('sample.txt', 'r') as file:
    content = file.read(30)
    print(content)