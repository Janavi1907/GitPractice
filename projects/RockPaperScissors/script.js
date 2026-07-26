let rock = document.getElementById("rock")
let paper = document.getElementById("paper")
let scissors = document.getElementById("scissors")
let choice = document.getElementById("choice")

rock.addEventListener("click", function () {
    choice.textContent = "Your Choice: Rock"
})
paper.addEventListener("click", function () {
    choice.textContent = "Your Choice: Paper"
})
scissors.addEventListener("click", function () {
    choice.textContent = "Your Choice: Scissors"
})
