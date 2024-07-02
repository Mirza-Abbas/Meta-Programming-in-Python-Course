def fn1():
	enclosed_v = 1
	
	#print(local_v) not accessible, throws error
	def fn2():
		local_v = 5
		print("Local Variable:", local_v) 
		print("Enclosed Variable:", enclosed_v) #accessible within nested functions
	fn2() #calling fn2 inside fn1
	
fn1()

#print(enclosed_v) not accessible outside, throws error
#print(local_v) not accessible outside, throws error