SELECT * FROM Join_Students;
SELECT * FROM departments;
SELECT J.Name,D.Department_Name
FROM Join_Students AS J
INNER JOIN departments AS D
ON J.Department_ID=D.Department_ID;