height = int(input("height of the person:  "))
credit = int(input("credit of the person:  "))
if height > 137 and credit > 10:
	print("Enjoy the ride!")
elif height < 137:
	print("You are not tall enough to ride")
elif credit < 10:
	print("You don't have enough credits")
else :
	print("you have not met the requirement")
