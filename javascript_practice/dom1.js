// PROGRAM 1
let head1=document.getElementById("title")
head1.textContent="Welcome to DOM Practice"

// PROGRAM 2
let div1=document.createElement("div")
div1.innerHTML="<h1>DOM Practice</h1><p>This is a practice for DOM manipulation.</p><button>Submit</button>"
document.body.appendChild(div1)

// PROGRAM 3
let head2=document.getElementById("subtitle")
head2.style.color="blue"
head2.style.backgroundColor="peachpuff"
head2.style.fontSize="22px"

// PROGRAM 4
let button1=document.querySelector("button")
button1.setAttribute("id","submitbutton")
button1.setAttribute("class","button_class")

// PROGRAM 5
console.log(button1.getAttribute("id"))
console.log(button1.getAttribute("class"))

// PROGRAM 6
let image=document.getElementById("photo")
image.setAttribute("src","https://picsum.photos/id/237/200/300")
image.setAttribute("width","200")

// PROGRAM 7
let para=document.createElement("p")
document.body.appendChild(para);
para.textContent="Hi everyone ,this is Janavi"
para.style.color="red"
para.style.fontWeight="bold"
para.style.fontSize="50px"
