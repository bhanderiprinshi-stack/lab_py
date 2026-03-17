#example 1:-basic leywprd argument
def student_info(name,age,city):
    print("name:",name)
    print("age:",age)
    print("city:",city)
student_info(age=18,city="rajkot",name="ravi")

#example 2:-mixing position and keyword
def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
display(1,c=3,b=2)

#exaple 3:-using keyword create function of simple interest
def simple_intrest(p:float,r:int,t:float):
    si=(p*r*t)/100
    print("simple intrest:",si)
simple_intrest(p=10000,t=1.5,r=2)
simple_intrest(t=1.5,p=15000,r=2)
