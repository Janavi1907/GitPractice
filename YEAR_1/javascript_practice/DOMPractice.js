// PROGRAM 1
let btn=document.getElementById("btn")
btn.addEventListener("click",function(e){
    document.body.style.backgroundColor="yellow"
    document.body.style.color="black"
})

// PROGRAM 2
let btn1=document.getElementById("btn1")
let para=document.getElementById("para")
btn1.addEventListener("click",function(e){
    if (para.style.display=="none") {
        para.style.display="block"
    } else {
        para.style.display="none"
    }
})

// PROGRAM 3
let count=0
let btn2=document.getElementById("btn2")
btn2.addEventListener("click",function(e){
    count++
    let para1=document.getElementById("para1")
    para1.textContent=count
})
let btn3=document.getElementById("btn3")
btn3.addEventListener("click",function(e){
    count--
    let para1=document.getElementById("para1")
    para1.textContent=count
})
btn4.addEventListener("click",function(e){
    count=0
    let para1=document.getElementById("para1")
    para1.textContent=count
})

// PROGRAM 4
let text=document.getElementById("text")
let textpara=document.getElementById("textpara")
text.addEventListener("input",function(event){
    textpara.textContent=event.target.value
})

// PROGRAM 5
let btn5=document.getElementById("btn5")
itemcount=0
btn5.addEventListener("click",function(e){
    itemcount++
    let list=document.getElementById("list")
    let li=document.createElement("li")
    li.textContent="Item "+itemcount
    list.appendChild(li)
})

// Challenge
let input=document.getElementById("input")
let btn6=document.getElementById("btn6")
let taskList=document.getElementById("taskList")
btn6.addEventListener("click",function(event){
    if(input.value!=""){
        let li=document.createElement("li")
        li.textContent=input.value
        taskList.appendChild(li)
        input.value=""
    }    
})

