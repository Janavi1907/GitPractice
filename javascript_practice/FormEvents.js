// PROGRAM 1
let input=document.getElementById("input")
input.addEventListener("input",function(event){
    console.log("Input Changed")
})

// PROGRAM 2
let para=document.getElementById("para")
input.addEventListener("input",function(event){
    para.innerText=event.target.value
    para.style.color="blue"
})

// PROGRAM 3
input.addEventListener("change",function(event){
    console.log("Final Value is "+event.target.value)
})

// PROGRAM 4
input.addEventListener("focus",function(event){
    input.style.backgroundColor="blue"
    input.style.color="white"
    console.log("Input Focused")
})

// PROGRAM 5
input.addEventListener("blur",function(event){
    input.style.backgroundColor=""
    input.style.color=""
    console.log("Input Lost Focus")
})

// CHALLENGE
let form=document.getElementById("form")
form.addEventListener("submit",function(event){
    event.preventDefault()
    console.log("Form Submitted Successfully") 
})

