#Reserve keywords such as print(), input() etc

print("Accessible Globally")

def fn1():
    print("Accessible inside function")
    
    def fn2():
        print("Accessible inside nested function")
    
    fn2()

fn1()