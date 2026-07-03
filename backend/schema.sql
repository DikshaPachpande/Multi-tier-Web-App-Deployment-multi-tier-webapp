CREATE DATABASE company;

USE company;

CREATE TABLE users(

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(50)

);

INSERT INTO users(name)
VALUES
('John'),
('Alice'),
('David'),
('Maria');
