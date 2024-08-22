class A:
    pass

class B(A):
    pass

class C:
    pass

a = A()
b = B()
c = C()

print(isinstance(a, A))
print(isinstance(b, A))
print(isinstance(c, A))
