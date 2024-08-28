#Exercise: Working with Methods

class A:
    def b(self):
        return "Function inside A"

class B:
    pass

class C:
    def b(self):
        return "Function inside C"

class D(B, C, A):
    pass

class D(C):
    pass

d = D()
print(d.b())

#D inherits b() from C
#Output: Function inside C