My_global = 10

print("Global Variable:", My_global) #accessible anywhere in the code

def fn1():
    print("Global Variable:", My_global) #also accessible within functions

fn1()