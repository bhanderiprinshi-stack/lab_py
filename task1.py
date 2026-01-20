#calculate simple intrest
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

#find maximumof two number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("Maximum number is:", num1)
else:
    print("Maximum number is:", num2)

#print number 1 to 5(range)
for i in range(1, 6):
    if i == 1 or i == 5:
        print(i)

#finf lenght of a string
text = input("Enter a string: ")
length = len(text)
print("Length of the string is:", length)

#print a welcome message
print("Welcome to Python Programming!")

#print first character of a string 
text = input("Enter a string: ")
print("First character is:", text[0])

#print last character of a string
text = input("Enter a string: ")
print("Last character is:", text[-1])

#check positive or negative numbers
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

#add three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
sum = num1 + num2 + num3
print("Sum of three numbers is:", sum)

#take a input from user
name = input("Enter your name: ")
print("Hello,", name)


