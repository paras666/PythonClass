def fun1():
	x1 = int(input("enter the number:"))
	x2 = int(input("enter the number:"))

	x3 = x2*x1

	return x3 

print("multiply",fun1())

def fun2():
	x1 = int(input("enter the number:"))
	x2 = int(input("enter the number:"))

	x3 = x2+x1

	return x3

print("addation",fun2())

def fun3():
	x1 = int(input("enter the number:"))
	x2 = int(input("enter the number:"))

	x3 = x1-x2

	return x3

print("subtraction",fun3())

def fun4():
	x1 = int(input("enter the number:"))
	x2 = int(input("enter the number:"))

	x3 = x1/x2

	return x3

print("division",fun4())

def fun5():
	x1 = int(input("enter the number"))
	x2 = int(input("enter the number"))

	x3 = pow(x1,x2)

	return x3

print("power",fun5()) 