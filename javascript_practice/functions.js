// PROGRAM 1
function intro(){
    console.log("Welcome to Javascript")
}
intro()
intro()
intro()

// PROGRAM 2
function printname(name){
    console.log("Hello " + name)
}
printname("Janavi")

// PROGRAM 3
function sumandsub(a,b){
    console.log("Sum: "+(a+b))
    console.log("Sub: "+(a-b))
}
sumandsub(4,5)
sumandsub(9,10)

// PROGRAM 4
function oddoreven(a){
    if (a%2==0){
        console.log(a+ " is a Even Number")
    }
    else {
       console.log(a+ " is a Odd Number") 
    }
}
oddoreven(0)
oddoreven(-2)
oddoreven(1)


// PROGRAM 5
function grade(marks){
    if (marks>=85){
        console.log("Distinction")
    }
    else if (marks>=60){
        console.log("First Class")
    }
    else if (marks>=35){
        console.log("Pass")
    }
    else{
        console.log("Fail")
    }
}
let m=prompt("Enter your marks: ")
m=Number.parseInt(m)
grade(m)

// PROGRAM 6
function square(X){
    return X*X
}
let result=square(5)
console.log("Square of 5 is "+ result)

// PROGRAM 7
function larger(a,b){
    if (a>b){
        return a
    }
    else{
        return b
    }
}
console.log("The largerest of two numbers is: "+ larger(15,7))
