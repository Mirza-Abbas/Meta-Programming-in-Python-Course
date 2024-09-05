animal = "camel"

def a():
    animal = "elephant"

    print("Inside function a(): " + animal)

def b():
    global animal
    animal = "elephant"  #This will now modify the global 'animal' variable

    print("Inside function b(): " + animal)

print("Before Calling a(): " + animal)
a() #No effect on the global 'animal' variable
print("After Calling a(): " + animal)
b() #Will modify the global 'animal' variable
print("After Calling b(): " + animal)