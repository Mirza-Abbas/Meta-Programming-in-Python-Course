print("Reading all content: \n")
with open('sample.txt', 'r') as file:
    content = file.readlines()
    print(content)

    print("\nLength:", len(content))

    for line in content:
        print(line, end='')