# marks in each subject#

x1= int(input("Entr marks of english: "))
x2= int(input("Entr marks of physics: "))
x3= int(input("Entr marks of maths: "))
x4= int(input("Entr marks of chemistry: "))
x5= int(input("Entr marks of physical: "))

total=x1+x2+x3+x4+x5

print("Total Sequred Marks:",total)
print("\n")

percent= total/5
print("Sequred Percentage:",percent,"%")
print("\n")

if(percent<33):
	print("Your are fail!!!")

elif((percent>33) and (percent<50)):
	print("3rd Division")

elif((percent>50) and (percent<60)):
	print("2nd Division")

else:
	print("1st Division")

