#create a dictionary of 3 studends with marks 
marks={
"janavi" :99,
"Meghana":11,
"geetha":87
}
print(marks)

#print names of students who scored above  80
for i,j in marks.items():
 if j>80:
    print(i)

#find the highest marks
maximum_marks=max(marks.values())
print (maximum_marks)


#Store name, USN, marks in dictionary
#Print grade using function 
def grade(marks):
  if marks>90:
    print("Grade:A")
  elif marks>75:
    print("Grade:B")
  elif marks>60:
    print("Grade:C")
  elif marks>45:
    print("Grade:D")
  else:
    print("Grade:F")

student={
  "janavi":{"usn":25001,"marks":99},
  "meghana":{"usn":25002,"marks":98},
  "geetha":{"usn":25003,"marks":46}
}
for name, details in student.items():
    print(f"{name}: ", end="")
    grade(details["marks"]) 