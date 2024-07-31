try:
    f_name = input('Type the file name: ')
    f = open(f_name)
    f_content = f.read()
    f_content_list = f_content.split("\n")
    f.close()
    print((f_content_list))
except FileNotFoundError as e:
    print("File is not found", e)