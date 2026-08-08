const student = {
  name: "Janavi S",
  USN: "1MV25CD026",
  marks: [86, 35, 87, 90, 99],
}
const { name, USN, marks } = student;
console.log(`Student Name : ${name}`);
console.log(`USN :${USN}`);
for (let i = 0; i < marks.length; i++) {
  console.log(`Subject ${i + 1} : ${marks[i]}`)
}
let total_marks = marks.reduce((m1, m2) => {
  return m1 + m2;
}, 0);
console.log(`Total Marks : ${total_marks}`);
console.log(`Average Marks : ${total_marks / marks.length}`)
console.log(`Percentage : ${((total_marks / 500)*100) .toFixed(2)}%`)
let isPass=true
marks.forEach(marks => {
    if(marks<35){
        isPass=false
    }
})
if (isPass) {
  console.log("Result : Pass");
} else {
  console.log(" Result : Fail");
}
