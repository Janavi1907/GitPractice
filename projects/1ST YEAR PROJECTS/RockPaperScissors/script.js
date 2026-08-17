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

let drawScore=0
let playerScore=0
let computerScore=0
let pScore = document.getElementById("pScore")
let dScore = document.getElementById("dScore")
let cScore = document.getElementById("cScore")
let result=document.getElementById("result")
buttons.forEach(function (button) {
    button.addEventListener("click", function () {
        let playerSelection = button.id.toLowerCase()
        let computerSelection = currentChoice.toLowerCase()
        let roundWinner=""
        if (playerSelection == computerSelection) {
            result.textContent = "🤝 Result: It's a Draw!"
            result.style.color="yellow"
            roundWinner="draw"
        } 
        else if (playerSelection=="rock"){
            if(computerSelection=="scissors"){
                result.textContent="🎉 Result: You Win!"
                result.style.color="green"
                roundWinner="player"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
                roundWinner="computer"
            }
        }
        else if (playerSelection=="paper"){
            if(computerSelection=="rock"){
                result.textContent="🎉 Result: You Win!"
                result.style.color="green"
                roundWinner="player"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
                roundWinner="computer"
            }
        }
        else if (playerSelection=="scissors"){
            if(computerSelection=="paper"){
                result.textContent="🎉 Result: You Win!"
                result.style.color="green"
                roundWinner="player"
            }else{
                result.textContent="❌ Result: You Lose!"
                result.style.color="red"
                roundWinner="computer"
            }
        }
        if (roundWinner=="player"){
            playerScore+=1
            pScore.textContent=playerScore
        }
        else if (roundWinner=="computer"){
            computerScore+=1
            cScore.textContent=computerScore
        }
        else if (roundWinner=="draw"){
            drawScore+=1
            dScore.textContent=drawScore
        }
    })           
})


let resetbtn=document.getElementById("resetbtn")
resetbtn.addEventListener("click",function(){
    result.textContent="Result:"
    result.style.color="#5A2A27"
    compChoice.textContent="Computer Choice:"
    choice.textContent="Your Choice:"
    playerScore=0
    computerScore=0
    drawScore=0
    pScore.textContent=0
    cScore.textContent=0
    dScore.textContent=0
})

