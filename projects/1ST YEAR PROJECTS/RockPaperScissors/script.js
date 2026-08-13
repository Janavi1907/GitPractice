let rock = document.getElementById("rock")
let paper = document.getElementById("paper")
let scissors = document.getElementById("scissors")
let choice = document.getElementById("choice")

rock.addEventListener("click", function (e) {
    choice.textContent = "Your Choice: Rock"
})
paper.addEventListener("click", function (e) {
    choice.textContent = "Your Choice: Paper"
})
scissors.addEventListener("click", function (e) {
    choice.textContent = "Your Choice: Scissors"
})

let choices=["Rock","Paper","Scissors"]
function computerChoice() {
    let randomChoice = Math.floor(Math.random() * choices.length)
    return choices[randomChoice]
}
let compChoice = document.getElementById("compChoice")
let buttons = document.querySelectorAll("button")
let currentChoice=""
buttons.forEach(function (button) {
    button.addEventListener("click", function () {
        currentChoice=computerChoice()
        compChoice.textContent = "Computer Choice: " + currentChoice
    })
})

let result=document.getElementById("result")
buttons.forEach(function (button) {
    button.addEventListener("click", function () {
        let playerSelection = button.id.toLowerCase()
        let computerSelection = currentChoice.toLowerCase()
        if (playerSelection == computerSelection) {
            result.textContent = "🤝 Result: It's a Draw!"
            result.style.color="yellow"
        } 
        else if (playerSelection=="rock"){
            if(computerSelection=="scissors"){
                result.textContent="🎉Result: You Win!"
                result.style.color="green"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
            }
        }
        else if (playerSelection=="paper"){
            if(computerSelection=="rock"){
                result.textContent="🎉 Result: You Win!"
                result.style.color="green"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
            }
        }
        else if (playerSelection=="scissors"){
            if(computerSelection=="paper"){
                result.textContent="🎉 Result: You Win!"
                result.style.color="green"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
            }
        }
    })           
})

