try:
    a = 5/0
except Exception as e:
    print("Something went wrong!", e)
    print(e.__class__)