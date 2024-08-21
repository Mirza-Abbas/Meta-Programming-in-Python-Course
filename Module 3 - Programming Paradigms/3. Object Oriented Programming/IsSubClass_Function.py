class A:
    pass

class B(A):
    pass

print(isinstance(A, B))
print(issubclass(B, A))