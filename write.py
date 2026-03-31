#1.write a single string
f=open("one.txt","w")
f.write("hello students\n")
f.write("welcome to python file handling\n")
f.write("learning is fun\n")
f.close()

#2.write with old data is erased
f=open("one.txt","w")
f.write("new content only.\n")
f.close()

#3.append mode
f=open("one.txt","a")
f.write("this line is addded at the and.\n")
f.close()

#4.writelines
f=open("one.txt","w")
lines=["python programing\n"
"file handling\n"
"error handling\n"
"exception handling\n"
]
f.writelines(lines)
f.close()