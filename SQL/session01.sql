#Q1
SELECT *FROM students;
SELECT Name FROM students;
SELECT Name,Marks FROM students;
SELECT * FROM students WHERE Department='CSE';
SELECT * FROM students WHERE Marks>80;

#Q2
SELECT * FROM students WHERE Marks>=85;
SELECT * FROM students WHERE Age=19;
SELECT * FROM students WHERE Department='CSE' AND Marks>85;
SELECT * FROM students WHERE Department='CSE' OR Department='ISE';
SELECT * FROM students WHERE Marks BETWEEN 75 AND 90;

#Q3
SELECT * FROM students WHERE Department IN ('CSE','ISE');
SELECT Name FROM students WHERE Marks IN (78, 85 ,88);
SELECT * FROM students WHERE Department NOT IN ('CSE');
SELECT * FROM students WHERE Age IN (19,20);
SELECT * FROM students WHERE Department NOT IN ('ISE','ECE');

