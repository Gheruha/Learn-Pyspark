-- Create a sandbox DB
CREATE DATABASE IF NOT EXISTS leet_spark;

USE leet_spark;

-- Table per problem statement
DROP TABLE IF EXISTS Courses;

CREATE TABLE Courses (
  student VARCHAR(50) NOT NULL,
  class VARCHAR(50) NOT NULL,
  PRIMARY KEY (student, class)
);

-- Sample data from the example
INSERT INTO
  Courses (student, class)
VALUES
  ('A', 'Math'),
  ('B', 'English'),
  ('C', 'Math'),
  ('D', 'Biology'),
  ('E', 'Math'),
  ('F', 'Computer'),
  ('G', 'Math'),
  ('H', 'Math'),
  ('I', 'Math');
