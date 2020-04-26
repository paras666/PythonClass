def fun1(x1,x2):
	
	x3=x1*x2
	return x3

print("multiply",fun1(2,2))

def fun2(x1,x2):

	x3=x1+x2
	return x3

print("addation",fun2(2,2))

def fun3(x1,x2):

	x3=x1-x2
	return x3

print("subtraction",fun3(2,2))

def fun4(x1,x2):

	x3=x2**x1
	return x3
print("power",fun4(2,2))

def fun5(x1,x2):

	x3=x2/x1
	return x3

print("division",fun5(2,2))

def fun6(x1):

	
	
	for x2 in range(1,11):
		x3=x2*x1
		print(x1,"*",x2,"=",x3)

		 

print("here you get",fun6(9))


