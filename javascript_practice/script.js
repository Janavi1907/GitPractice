// PROGRAM 1
for (let a = 1; a <= 10; a++) {
    console.log(a)
}

// PROGRAM 2
for (let b = 10; b >= 1; b--) {
    console.log(b)
}

// PROGRAM 3
for (let c = 2; c <= 50; c+=2) {
    console.log(c)
}

// PROGRAM 4
for (let d = 1; d <= 50; d+=2) {
    console.log(d)
}

// PROGRAM 5
let n=prompt("Enter a number: ")
n=Number.parseInt(n)
for (let i=1; i<=10; i++) {
    console.log(n + " X " + i + " = " + (n * i))
}

// PROGRAM 6
let sum=0
for (let e=1; e<=100 ; e++) {
    sum += e
}
console.log(sum)

// PROGRAM 7
let f=1
while(f<=20){
    console.log(f)
    f++
}

// PROGRAM 8
let j=1
do{
    console.log(j)
    j++
}while(j<=5)