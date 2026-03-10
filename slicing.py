#1.basic slices
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])

#2.slicing with step
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#3.negative slicing
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#4.reverse array using slicing
arr=array('i',[10,20,30,40,50])
print(arr[::-1])

#5.modifying slices
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)