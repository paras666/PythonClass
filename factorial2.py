x = int(input("enter the number to find factorial: "))
y = 1

for z in range(x,1,-1):
	print(z*y,"x",z-1)
	y = y*z

print("your factorial is",y)

if(x<=1):
	print(1)
