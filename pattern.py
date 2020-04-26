x = int(input("enter the number to define star limit:  "))


for m in range(0,x+1):
	for n in range(0,m+1):
		print(end = " ")

	for n in range(0,x-m-1):
		print("*",end = " ")

	print()

for y in range(0,x):
	for z in range(0,x-y-1):
		print(end=" ")
	
	for z in range(0,y+1):
		print("*",end=" ")
	
	print()
