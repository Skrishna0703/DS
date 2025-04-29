-- Step 1: Create database
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

-- Step 2: Create table
CREATE TABLE IF NOT EXISTS students (
    roll_no INT,
    name STRING,
    age INT,
    department STRING,
    marks DOUBLE
)
STORED AS PARQUET;

-- Step 3: Insert data
INSERT INTO students VALUES (1, 'Alice', 20, 'Computer Science', 85.5);
INSERT INTO students VALUES (2, 'Bob', 21, 'Mechanical', 78.0);

-- Step 4: Query data
SELECT * FROM students;
