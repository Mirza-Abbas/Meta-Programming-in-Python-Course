try:
    b = 3/a
except ZeroDivisionError as e:
    print(e, "Cannot divide by zero")
except Exception as e:
    print("Something went wrong.", e)
    print(e.__class__)