// PROGRAM 1
let btn=document.getElementById("btn")
btn.addEventListener("click",function(){
    console.log("Buttom Clicked!")
})

// PROGRAM 2
let btn1=document.getElementById("btn1")
btn1.addEventListener("click",function(){
    btn1.style.backgroundColor="red"
    btn1.style.color="white"
})

//PROGRAM 3
let btn2=document.getElementById("btn2")
let count=0
btn2.addEventListener("click",function(){
    count++
    console.log("Button clicked "+count)
})

// PROGRAM 4
let btn3=document.getElementById("btn3")
btn3.addEventListener("click",function(){
    console.log("Button Clicked1")
})
btn3.addEventListener("click",function(){
    console.log("Button Clicked2")
})

// PROGRAM 5
let box=document.getElementById("box")
box.style.width="100px"
box.style.height="100px"
box.style.border="2px solid black"
box.style.display="flex"
box.style.justifyContent="center"
box.style.alignItems="center"
box.addEventListener("mouseover",function(){
    box.style.backgroundColor="blue"
    box.style.color="white"
})
box.addEventListener("mouseout",function(){
    box.style.backgroundColor="white"
    box.style.color="black"
})

