#Hello, there!
#This program is created by Dev Ali
#Dev Ali (me) is a beginner Python Programmer
#Program to print tables

#The number you want the table of
num = input("Enter the number: ")

#Converts the number into an integer
try:
	num = int(num)
except:
	print("Sorry! You did not enter a number")
	exit()

#The times you want
times = int(input("Times: "))

#Main function
x = 0
while x < times:
	x = x + 1
	print(num, "*", x, "=", num * x)