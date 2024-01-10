DROP DATABASE IF EXISTS movies_db;
CREATE DATABASE movies_db;

USE movies_db;


CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year YEAR,
    plot TEXT
);