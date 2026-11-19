SELECT * FROM students;
#PART A
SELECT COUNT(*) AS Total_Students FROM students;
SELECT SUM(Marks) AS Total_marks FROM students;
SELECT AVG(Marks) AS Average_marks FROM students;
SELECT MIN(Marks) AS Lowest_marks FROM students;
SELECT MAX(Marks) AS Highest_marks FROM students;
SELECT COUNT(Name) AS Total_Students_by_Name FROM students;

#PART B
SELECT COUNT(*) AS Total_Students_CSE FROM students WHERE Department='CSE' ; 
SELECT AVG(Marks) AS Average_Marks_CSE FROM students WHERE Department='CSE' ; 
SELECT MAX(Marks) AS Highest_Marks_ISE FROM students WHERE Department='ISE' ; 
SELECT SUM(Marks) AS Total_Marks_ECE FROM students WHERE Department='ECE' ; 
SELECT COUNT(*) AS Marks_greater_80 FROM students WHERE Marks>80 ; 

#PART C
SELECT
COUNT(*) AS Total_no_STD,
AVG(Marks) AS Avg_marks
FROM students;
SELECT
SUM(Marks) AS Total_marks,
MIN(Marks) AS Lowest_marks,
MAX(Marks) AS Highest_marks 
FROM students;
SELECT 
COUNT(*) AS Total_Students,
SUM(Marks) AS Total_marks,
AVG(Marks) AS Average_marks,
MIN(Marks) AS Lowest_marks,
MAX(Marks) AS Highest_marks,
COUNT(Name) AS Total_Students_by_Name
FROM students;