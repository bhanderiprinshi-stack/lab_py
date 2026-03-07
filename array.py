#example 1:integer array

from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

#basic  array opreations

#1.len()-number of element
from array import array
arr=array('i')

#2.append()-add element at and
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#3.insert(pos,x)-insert at positing
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#4.remove-remove first occurence
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#5.pop()-remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#6.index-find index of elemnet
arr=array('i',[10,20,30,40])
print(arr.index(30))

#7.count()-count occurrences
arr=array('i',[10,20,30,40])
print(arr.count(20))

#8.reverse-reverse array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)
