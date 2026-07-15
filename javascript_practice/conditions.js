//PROGRAM 1 
let a=prompt("Enter a number:") 
if(a>0){ 
    console.log("Positive number") 
} 
else if(a==0){
    console.log("Zero") 
} 
else{
    console.log("Negative Number") 
} 

//PROGRAM 2
let b=prompt("Enter a Number:") 
if(b%2==0){ 
    console.log("Even Number") 
} else{ 
    console.log("Odd Number") 
}

//PROGRAM 3
let age=prompt("Enter your age:") 
if (age>=18){ 
    console.log("Eligible to vote") 
} 
else{ 
    console.log("not eligible to vote") 
} 

//PROGRAM 4 
let marks=prompt("Enter your marks:") 
if (marks>=90){ 
    console.log("Grade A") 
} 
else if(marks>=70){ 
    console.log("Grade B") 
} 
else if (marks>=50){ 
    console.log("Grade C") 
} 
else { 
    console.log("Fail") 
}
 
//PROGRAM 5 
let num1=prompt("Enter first number:") 
let num2=prompt("Enter second number:") 
if(num1>num2){ 
    console.log("Greater number is:" + num1) 
} 
else if(num1==num2){ 
    console.log("Both numbers are equal") 
} 
else{ 
    console.log("Greater number is:" + num2) 
} 