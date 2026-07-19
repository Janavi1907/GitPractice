// PROGRAM 1
let btn=document.getElementById("btn")
btn.onclick=()=>{
    console.log("Welcome Janavi")
}

// PROGRAM 2
let btn1=document.getElementById("btn1")
document.body.ondblclick=function(){
    document.body.style.backgroundColor="yellow"
    document.body.style.color="black"
}

// PROGRAM 3
let box=document.createElement("div")
box.textContent="Box 1"
box.style.width="100px"
box.style.height="100px"    
box.style.border="2px solid black"
document.body.appendChild(box)
box.onmouseover=()=>{
    box.style.backgroundColor="blue"
    box.style.color="white"
}

// PROGRAM 4
box.onmouseout=()=>{
    box.style.backgroundColor="white"
    box.style.color="black"
}

// PROGRAM 5
let btn2=document.getElementById("btn2")
btn2.onclick=()=>{
    console.log("Good Morning")
}
let btn3=document.getElementById("btn3")
btn3.onclick=()=>{
    console.log("Good Evening")
}
