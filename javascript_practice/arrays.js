// PROGRAM 1
let fruits=["Strawberry","Mango","Banana","Apple","Grapes"]
console.log(fruits)

// PROGRAM 2
let numbers=[11,33,56,47,89,44,89.8]
console.log(numbers[0])
console.log(numbers[6])

// PROGRAM 3
let names=["Janavi","Riya","Sakshi","Pooja"]
names[2]="Megha"
console.log(names)

// PROGRAM 4
let colors=["Red","Green","Blue","Yellow"]
console.log("The length of the array is: "+colors.length)

// PROGRAM 5
let animals=["Dog","Cat","Cow","Lion"]
let n=animals.length
for(let i=0;i<n;i++){
    console.log(animals[i])
}

// PROGRAM 6
let marks=[45,67,89,90,78]
let m=marks.length
let sum=0
for(let j=0;j<m;j++){
    sum+=marks[j]
}
let average=sum/m
console.log("The sum of marks is: "+sum)
console.log("The average marks is: "+average)

// PROGRAM 7
let no = [1, 2, 3, 4, 5]
let largest = no[0] 
for (let k = 1; k < no.length; k++) {
    if (no[k] > largest) {
        largest = no[k]
    }
}
console.log("The largest number is: " + largest)

// PROGRAM 8
let digits = [10, 25, 32, 48, 50]
let smallest = digits[0]
for (let l = 1; l < digits.length; l++) {
    if (digits[l] < smallest) {
        smallest = digits[l]
    }
}
console.log("The smallest number is: " + smallest)

