#print message
x="hello world"
print(x)
# add two number
x=12
b=15
print(x+b)
# even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The given number is Even")
else:
    print("The given number is Odd")
# check leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) :
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
# Program to print value of pi

import math

print("Value of pi is:", math.pi)
# Program to store and print gravity constant

GRAVITY = 9.8   # gravity in m/s^2

print("The value of gravity is:", GRAVITY, "m/s^2")
# Program to find square of a number

num = int(input("Enter a number: "))

square = num * num

print("Square of the number is:", square)
# Program to find area of a square

side = float(input("Enter the side of the square: "))

area = side * side

print("Area of the square is:", area)
# Program to check data type

value = input("Enter any value: ")

print("The data type is:", type(value))
# Program using math functions

import math

num = float(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Ceil value:", math.ceil(num))
print("Floor value:", math.floor(num))
print("Factorial:", math.factorial(int(num)))
#find a power
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power: "))

result = base ** exponent
print("Result =", result)
#check positive or negative
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")