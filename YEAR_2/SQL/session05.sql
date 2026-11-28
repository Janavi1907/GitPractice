SELECT * FROM join_students;
SELECT * FROM departments;
#Q1
SELECT join_students.Name,departments.Department_Name
FROM join_students
INNER JOIN departments
ON join_students.department_ID=departments.department_id
WHERE Department_Name='CSE';

#Q2
SELECT join_students.Name,departments.Department_Name
FROM join_students
INNER JOIN departments
ON join_students.department_ID=departments.department_id
WHERE Department_Name='ISE';

#Q3
SELECT join_students.Name,departments.Department_Name
FROM join_students
INNER JOIN departments
ON join_students.department_ID=departments.department_id
WHERE Department_Name='CSE' or  Department_Name='ECE';