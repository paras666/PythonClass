def fun1 ( x )
	if x==1:
		return 1

	else:
		return x * fun1(x-1)

print(factorial(5))