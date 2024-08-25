#Mixes characteristics of multiple inheritance types.

class Parent:
    a = 5

class ChildA(Parent):
    b = 10

class ChildB(Parent):
    b = 0

class GrandChild(ChildB):
    c = 100

gc = GrandChild()

print(gc.a, gc.b, gc.c)