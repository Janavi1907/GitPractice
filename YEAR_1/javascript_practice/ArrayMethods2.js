// PROGRAM 1
let arr=[15,25,40,55,70,90]
let filtered_arr=arr.filter((value)=>{
    return value>=50
})
console.log(filtered_arr)

// PROGRAM 2
let ages=[19,12,10,4,5,60,45]
let adults=ages.filter((age)=>{
    return age>=18
})
console.log(`People above 18years are: ${adults}`)

// PROGRAM 3
let fruits=["Apple","Banana","Mango","Orange"]
let find_mango=fruits.find((fruit)=>{
    return fruit=="Mango"
})
console.log(find_mango)

// PROGRAM 4
let numbers=[11,22,33,44,55]
let find_44=numbers.find((number)=>{
    return number==44
})
console.log(find_44)

// PROGRAM 5
let arr1=[5,10,15,20]
let total1=arr1.reduce((x1,x2)=>{
    return x1+x2
},0)
console.log(`Total sum is: ${total1}`)

// PROGRAM 6
let arr2=[85,92,70,88,95]
let total2=arr2.reduce((x,y)=>{
    return x+y
}) 
console.log(`Total sum is: ${total2}`)
console.log(`Average is: ${total2/arr2.length}`)



