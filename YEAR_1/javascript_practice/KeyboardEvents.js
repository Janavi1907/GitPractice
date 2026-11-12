// PROGRAM 1
document.addEventListener("keydown",function(event){
    console.log("Key pressed")
})

// PROGRAM 2
document.addEventListener("keydown",function(event){
    console.log("Key pressed: "+event.key)
})

// PROGRAM 3
document.addEventListener("keydown",function(event){
    console.log("Event Code: "+ event.code)
})

// PROGRAM 4
document.addEventListener("keyup",function(event){
    console.log("Key Released")
})

// PROGRAM 5
let userType=document.getElementById("userType")
userType.addEventListener("keydown",function(event){
    console.log("You Typed: "+event.key)
})

// CHALLENGE QUESTION
document.addEventListener("keydown",function(event){
    if (event.key=="Enter") {
        console.log("Form Submitted")
    }
    else if(event.key=="Escape") {
        console.log("Cancelled")

    }
})

