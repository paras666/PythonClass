x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))


if(x<y<z):
	print("x < y < z")

elif(y<z<x):
	print("y < z < x")

else:
	print("z < x < y")