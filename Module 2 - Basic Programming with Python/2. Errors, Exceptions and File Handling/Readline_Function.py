print("Reading a single line: \n")
with open('sample.txt', 'r') as file:
    content = file.readline()
    print(content)

print("Reading Specific Characters in a single line: \n")
with open('sample.txt', 'r') as file:
    content = file.readline(10)
    print(content)