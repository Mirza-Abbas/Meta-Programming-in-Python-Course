f = open("petnames.txt", "r")

f_content = f.read()

f_content_list = f_content.split("\n")

f.close()

print(f_content_list)