// PROGRAM 1
let student={
    "Name":"Janavi",
    "Age":18,
    "Branch":"CSE-DS",
    "Semester":2
}
console.log(student)

// PROGRAM 2
console.log(student.Name)
console.log(student["Name"])
console.log(student.Branch)
console.log(student["Branch"])

// PROGRAM 3
student.Age=20
console.log(student.Age)

// PROGRAM 4
student.College="SIR MVIT"
console.log(student)

// PROGRAM 5
let mobile={
    "Brand":"Redmi",
    "Model":"13 5G",
    "Price":15000,
    "color":"Blue"
}
for(let key in mobile){
    console.log(key + " : " + mobile[key])
}

// PROGRAM 6
let book={
    "Name":"Javascript",
    "Author":"John Doe",
    "Price":500,
    "Publisher":"ABC Publications"
}
book.Price=600
book.year=2023
console.log(book)

// PROGRAM 7
for (let detail in student){
    console.log(detail + " : " + student[detail])
}

// PROGRAM 8
let myself={
    "Name":"Janavi",
    "Age":18,
    "College":"SIR MVIT",
    "Branch":"CSE-DS",
    "Semester":2,
    "Favourite language":"Python",
    "Favourite subject":"CS"
}
for (let self in myself){
    console.log(self + " : " + myself[self])
}

