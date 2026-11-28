SELECT * FROM join_students;
SELECT * FROM departments;

#Q1
SELECT s.Name,d.Department_Name
FROM join_students AS s 
LEFT JOIN departments AS d
ON s.department_ID=d.department_ID;

#Q2
SELECT s.Name,d.Department_Name
FROM join_students AS s 
LEFT JOIN departments AS d
ON s.department_ID=d.department_ID
WHERE d.department_Name IS NULL;

#Q3
SELECT s.Name,d.Department_Name
FROM join_students AS s 
RIGHT JOIN departments AS d
ON s.department_ID=d.department_ID;

#Q4
SELECT s.Name,d.Department_Name
FROM join_students AS s 
RIGHT JOIN departments AS d
ON s.department_ID=d.department_ID
WHERE s.Name IS NULL;