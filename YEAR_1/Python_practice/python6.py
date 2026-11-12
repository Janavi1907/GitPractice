#Create a file called myfile.txt and write:
#I am learning Python
f=open("myfile.txt","w")
f.write("I am Learning python")
f.close()


#Read the content of myfile.txt and print it.
f=open("myfile.txt","r")
print(f.read())
f.close()


#Append your name to the same file.
f=open('myfile.txt','a')
f.write("\tJanavi")
f.close()

f=open("myfile.txt","r")
print(f.read())
f.close()
