try:
    with open('sample/newfile.txt', 'w') as file:
        file.write("Test File")
except FileNotFoundError as e:
    print("Error: ", e)