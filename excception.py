#1.example of excception
try:
    num1=int(input("enter a number:"))
    num2=int(input("enter another number:"))
    result=num1/num2

except ZeroDivisionError:
        print("you cannot divide by zero!")

except valueEroor:
        print("please enter a valid number")
else:
        print("division successful result is:",result)
finally:
        print("this block always runs")

#2.exaple of excception
try:
    my_list=[1,2,3]
    print(my_list[1])

except IndexError:
    print("index is out of range")

else:
    print("element found successfully!")

finally:
    print("programe finished")