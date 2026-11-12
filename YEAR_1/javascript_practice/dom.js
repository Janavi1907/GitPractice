// PROGRAM 1
let heading=document.getElementById("title")
console.log(heading.textContent)

// PROGRAM 2
let para=document.getElementsByClassName("text")
console.log(para[0].textContent)
console.log(para[1].textContent)

// PROGRAM 3
let button=document.getElementsByTagName("button")
 for (let i = 0; i < button.length; i++) {   //using for loop 
    console.log(button[i].textContent)
}

// PROGRAM 4
let h2=document.querySelector("#subtitle")
console.log(h2.textContent)
let para1=document.querySelector(".text")
console.log(para1.textContent)

// PROGRAM 5
let allPara=document.querySelectorAll(".text")
console.log(allPara[0].textContent)
console.log(allPara[1].textContent)
let allButton=document.querySelectorAll("button")
console.log(allButton[0].textContent)
console.log(allButton[1].textContent)
console.log(allButton[2].textContent)

// PROGRAM 6
let h1=document.querySelector("#title")
console.log(h1.textContent)
let p1=document.querySelector(".text")
console.log(p1.textContent)
let button1=document.querySelector("button")
console.log(button1.textContent)
let div1=document.querySelector("div")
console.log(div1.textContent)
