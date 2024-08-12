data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

new_data = {x - 1 for x in data if x > 5}

print(new_data)