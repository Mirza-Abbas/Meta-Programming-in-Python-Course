def a():
    animal = "camel"

    def b():
        nonlocal animal
        animal = "elephant" #This will now modify the Enclose 'animal' variable

        print("Inside Nested Function b(): " + animal)

    print("Before Function b(): " + animal)
    b()
    print("After Function b(): " + animal)

a()