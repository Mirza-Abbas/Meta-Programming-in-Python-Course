#Concerns how several sub classes inherit from a common parent.

class Parent:
    a = 10

class ChildA(Parent):
    b = 5

class ChildB(Parent):
    a = 0
    b = 100

c1 = ChildA()
c2 = ChildB()

print(c1.a, c1.b)
print(c2.a, c2.b)