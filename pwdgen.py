import random
low="abcdefghijklmnopqrstuvwxyz"
upp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nos="01234567890"
sym="!@#$%^&*()_-{}[];:"
all=low+upp+nos+sym
#exit="E"
while exit!="E":
	length=int(input("Enter the Length of the Password:   "))
	password="".join(random.sample(all,length))
	print("Your Password is :  ",password)
	exit=input("Enter 'E' to exit or to continue press 'N':  ")
	#print("Enter 'E' to exit")

