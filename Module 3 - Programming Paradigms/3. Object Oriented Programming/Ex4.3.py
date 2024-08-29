#Exercise: Working with Methods

class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a())

#Python first looks for a() in C, then in B & then in A
#When a() is not found, it throws error

#Output: Attribute Error