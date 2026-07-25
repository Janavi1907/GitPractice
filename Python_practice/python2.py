#A function to add two numbers 
def sum(a,b):
    print("Sum:",a+b)
c=int(input("Enter first number:"))
d=int(input("Enter second number:"))
sum(c,d)

#A function to check if the number is even or odd
def evenorodd(x):
    x=int(x)
    if(x%2==0):
        print(x,"is even number")
    else:
        print(x,"is odd number")
a=input("Enter a number:")
evenorodd(a)

#a function that retuns a student grade based on marks 
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
marks = int(input("Enter marks: "))
grade = get_grade(marks)
print("Grade:", grade)
