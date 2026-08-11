let button=document.getElementById("btn")
let nameOutput=document.getElementById("name-output-value")
let USNOutput=document.getElementById("USN-output-value")
let totalMarksOutput=document.getElementById("total-marks-value")
let averageOutput=document.getElementById("average-value")
let percentageOutput=document.getElementById("percentage-value")
let resultOutput=document.getElementById("result-value")
let resultContainer=document.getElementById("result-container") 
button.addEventListener("click",function(){
    nameOutput.textContent=document.getElementById("name").value
    USNOutput.textContent=document.getElementById("USN").value
    if(nameOutput.textContent=="" || USNOutput.textContent==""){
      alert("Please enter Name and USN.");
      resultContainer.style.display = "none";
      return;
    }
    let marks1 = document.getElementById("sub_marks1").value
    let marks2 = document.getElementById("sub_marks2").value
    let marks3 = document.getElementById("sub_marks3").value
    let marks4 = document.getElementById("sub_marks4").value
    let marks5 = document.getElementById("sub_marks5").value
    if(marks1=="" || marks2=="" || marks3=="" || marks4=="" || marks5==""){
      alert("Please enter all marks.");
      resultContainer.style.display = "none";
      return;
    }
    let val1=Number(marks1)
    let val2=Number(marks2)
    let val3=Number(marks3)
    let val4=Number(marks4)
    let val5=Number(marks5)
    if(val1 < 0 || val1 > 100 || 
      val2 < 0 || val2 > 100 || 
      val3 < 0 || val3 > 100 || 
      val4 < 0 || val4 > 100 || 
      val5 < 0 || val5 > 100) {
      alert("Please enter a marks between 0 to 100.");
      return; 
    }
    const marks=[val1,val2,val3,val4,val5]
    let total_marks = marks.reduce((m1, m2) => {
    return m1 + m2;
    }, 0);
    totalMarksOutput.textContent=total_marks
    averageOutput.textContent=(total_marks/marks.length).toFixed(2)
    percentageOutput.textContent=((total_marks/500)*100).toFixed(2)
    let isPass=true
    marks.forEach(mark => {
        if(mark<35){
            isPass=false
        }
    })
    if (isPass) {
      resultOutput.textContent="PASS"
      resultOutput.style.color="green"
    } else {
      resultOutput.textContent="FAIL"
      resultOutput.style.color="red"
    }
    resultContainer.style.display="block"
    resultContainer.scrollIntoView({
      behavior: "smooth",
      block:"center"
    })
})


