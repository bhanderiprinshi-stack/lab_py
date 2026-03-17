#example 1:-basic positional arguments
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

#example 2:-student infprmation
def student_info(name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)

student_info("ravi",101,85)

#simple inerest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest:",si)
simple_interest(1000,2,2)
simple_interest(50000,1.2,3)

#area of circle
def ar_circle(r):
    ar_circle=3.14*r*r
    print("area of circle:",ar_circle)
ar_circle(1.5)
ar_circle(4)

#check number positive negative or zero
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(90)
check_value(-15)

#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value{no}is even ")
    else:
        print(f"value{no}id odd")
odd_even(50)
odd_even(15)

#arithmetic opretion substraction,multipication and division
def addition(a,b):
    add=a+b
    print("arithmetic of two values",add)
addition(50,10.5)
addition(100,200)
