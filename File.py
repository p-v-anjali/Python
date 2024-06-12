#f = open("File1.txt","x")
#to create a file File1.txt 

#f = open("abc.txt","x")
f = open("abc.txt","w")
f.write("Hello from a file ")


f = open("abc.txt","a")
f.write("Hi ")

f = open ("abc.txt","r")

print(f.read())

