def fn1():
    local_v = 10
    print("Local Variable:", local_v) #accessible inside function

fn1()

#not accessible outside function, throws error:
#print(local_v) 