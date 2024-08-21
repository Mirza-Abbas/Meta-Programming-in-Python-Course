class A: 
    a = 7

class B(A): 
    a = 8

class C(B):
    a = 9

a = A()
b = B()
c = C()

print(a.a)
print(b.a)
print(c.a)