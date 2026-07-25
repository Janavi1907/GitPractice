# Open file in append mode to add new student records
f= open('students.txt', 'a')
for i in range(1,4):
        name = input(f"Enter student name {i}: ")
        marks = input(f"Enter student marks{i} : ")
        i+1
f.write(f"{name},{marks}\n")
print("Student data saved successfully!")
f.close()

f=open('students.txt','r')
print(f.read())
f.close()