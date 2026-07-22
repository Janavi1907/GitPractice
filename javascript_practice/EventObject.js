// PROGRAM 1
let btn=document.getElementById("btn")
btn.addEventListener("click",function(event){
    console.log(event)
})

// PROGRAM 2
btn.addEventListener("click",function(event){
    console.log(event.type)
})

// PROGRAM 3
btn.addEventListener("click",function(event){
    console.log(event.target)
})

// PROGRAM 4
let btn1=document.querySelectorAll("button")
btn1.forEach(function(button){
    button.addEventListener("click",function(event){
        console.log("You Clicked button "+event.target.textContent)
    })
})

// PROGRAM 5
let box=document.getElementById("box")
box.style.width="100px"
box.style.height="100px"
box.style.border="2px solid black"
box.style.alignItems="center"
box.style.justifyContent="center"
box.style.display="flex"
box.addEventListener("click",function(event){
    console.log("Clicked inside the box")
})

