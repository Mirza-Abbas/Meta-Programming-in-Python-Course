try:
    a = 5/0
except ZeroDivisionError as e:
    print("Something went wrong!", e)