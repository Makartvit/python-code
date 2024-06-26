-- CREATE TABLE departments (
--     department_id SERIAL PRIMARY KEY,
--     department_name VARCHAR(255) NOT NULL
-- );
-- CREATE TABLE teachers (
--     teacher_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(255) NOT NULL,
--     last_name VARCHAR(255) NOT NULL,
--     department_id INT,
--     FOREIGN KEY (department_id) REFERENCES departments(department_id)
-- );
-- CREATE TABLE groups (
--     group_id SERIAL PRIMARY KEY,
--     group_name VARCHAR(100) NOT NULL,
--     department_id INT,
--     FOREIGN KEY (department_id) REFERENCES departments(department_id)
-- );
-- CREATE TABLE students (
--     student_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(255) NOT NULL,
--     last_name VARCHAR(255) NOT NULL,
--     group_id INT,
--     FOREIGN KEY (group_id) REFERENCES groups(group_id)
-- );
-- INSERT INTO departments (department_name) VALUES
-- ('Computer Science'),
-- ('Mathematics'),
-- ('Physics');
-- INSERT INTO teachers (first_name, last_name, department_id) VALUES
-- ('John', 'Doe', 1),
-- ('Jane', 'Smith', 2),
-- ('Robert', 'Johnson', 3),
-- ('Emily', 'Williams', 1),
-- ('Michael', 'Brown', 2);
-- INSERT INTO groups (group_name, department_id) VALUES
-- ('CS50', 1),
-- ('Math101', 2),
-- ('Phys101', 3),
-- ('CS101', 1);
-- INSERT INTO students (first_name, last_name, group_id) VALUES
-- ('Alice', 'Johnson', 1),
-- ('Bob', 'Smith', 2),
-- ('Charlie', 'Williams', 3),
-- ('David', 'Brown', 1),
-- ('Eva', 'Davis', 2),
-- ('Frank', 'Miller', 3),
-- ('Grace', 'Jones', 4),
-- ('Henry', 'Anderson', 1),
-- ('Ivy', 'Moore', 2),
-- ('Jack', 'Taylor', 3),
-- ('Kate', 'White', 4),
-- ('Leo', 'Martin', 1),
-- ('Mia', 'Young', 2),
-- ('Noah', 'Lee', 3),
-- ('Olivia', 'Harris', 4),
-- ('Paul', 'Clark', 1),
-- ('Quinn', 'Evans', 2),
-- ('Ryan', 'Wright', 3),
-- ('Sophia', 'Walker', 4),
-- ('Tyler', 'Hill', 1);
-- SELECT 
--     s.first_name, 
--     s.last_name, 
--     g.group_name
-- FROM 
--     students s
-- JOIN 
--     groups g ON s.group_id = g.group_id;
-- SELECT 
--     t.first_name,
--     t.last_name,
--     d.department_name
-- FROM 
--     teachers t
-- JOIN 
--     departments d ON t.department_id = d.department_id;
-- SELECT 
--     g.group_name,
--     COUNT(s.student_id) AS student_count
-- FROM 
--     groups g
-- LEFT JOIN 
--     students s ON g.group_id = s.group_id
-- GROUP BY 
--     g.group_name
-- ORDER BY 
--     g.group_name;
-- SELECT 
--     d.department_name,
--     t.first_name AS teacher_first_name,
--     t.last_name AS teacher_last_name,
--     g.group_name,
--     s.first_name AS student_first_name,
--     s.last_name AS student_last_name
-- FROM 
--     teachers t
-- JOIN 
--     departments d ON t.department_id = d.department_id
-- JOIN 
--     groups g ON t.department_id = g.department_id
-- LEFT JOIN 
--     students s ON g.group_id = s.group_id
-- WHERE 
--     t.last_name IN ('Smith', 'Williams', 'Johnson')
-- ORDER BY 
--     g.group_name, s.last_name;


