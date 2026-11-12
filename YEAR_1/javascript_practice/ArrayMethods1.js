// PROGRAM 1
let fruits=["Apple","Banana","Mango","Grapes","Orange"]
fruits.forEach((fruit)=>{
    console.log(fruit)
})

// PROGRAM  2
let a=[5,10,15,20,25]
a.forEach((value)=>{
    value=value*2
    console.log(value)
})


// PROGRAM 3
let marks=[50,60,70,80,90]
let updatedMarks= marks.map((element)=>{
    return element+5
})
console.log(marks)
console.log(updatedMarks)

// PROGRAM 4
let temp=[30,32,35,40,45]
let fahrenheit=temp.map((element)=>{
    return (element*(9/5))+32
})
console.log(fahrenheit)

// PROGRAM 5
let names=["Janavi","Meghu","Sakshi","Joe"]
let upperNames=names.map((element)=>{
    return element.toUpperCase()   
})
console.log(upperNames)

