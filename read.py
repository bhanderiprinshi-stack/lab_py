#1.reading text file
f=open("one.txt","r")
data=f.read()
print("file content",data)
f.close()

#2.reading specific number of characters
f=open("one.txt","r")
data=f.read(10)
print("first part:",data)
f.close()

#3.readlines
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line1",line1)
print("line2",line2)
print("line3",line3)
f.close()

#4.read all lines into a list
f=open("one.txt","r")
lines=f.readlines()
print("list of lines",lines)
print("number of lines",len(lines))
f.close()

#5.read specific line in file
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()