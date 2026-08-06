// PROGRAM 1
// 1.Normal function 
function add(x,y){
    let sum=x+y
    console.log(sum)
}
add(11,50)
// 2.Arrow function 
const addno=(a,b)=>{
    let sum=a+b
    console.log(sum)
}
addno(11,50)

// PROGRAM 2
const name = "Janavi";
const branch = "CSE-DS";
const college = "Sir MVIT";
console.log("My name is "+ name+" and my branch is "+ branch+" in "+ college) //1.using+
console.log(`My name is ${name} and my branch is ${branch} in ${college}`) //2.using template literals

// PROGRAM 3
let student = {
    name: "Janavi",
    usn: "1MV25CD026",
    branch: "CSE-DS"
}
let {name,usn,branch}=student
console.log(name)
console.log(usn)
console.log(branch)

// PROGRAM 4
let a=[1,3,4,5,7,3]
let b=[1,2,3,4,5,6]
let c=[...a , ...b]
console.log(c)

// PROGRAM 5
function sum(...numbers){
    let total=0
    for(let number of numbers){
        total=total+number
    }
    console.log(total)
}
sum(1,2,4,90,2,2,3,4,4)


