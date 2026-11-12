SELECT * FROM students;
#T1
SELECT * FROM students WHERE Name LIKE 'S%';
#T2
SELECT * FROM students WHERE Name LIKE '%a';
#T3
SELECT * FROM students WHERE Name LIKE '%ri%';
#T4
SELECT * FROM students WHERE Name NOT LIKE 'A%';
#T5
SELECT * FROM students WHERE Name LIKE 'K____';
#T6
SELECT * FROM students WHERE Name NOT LIKE '%a';