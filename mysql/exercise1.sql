-- Exercise src/dataframe_api/exercise1 done in MySQL
/*
Goal: From employees table, build a cleaned view of people hired since 2000-01-01, compute their tenure, bucket them into bands, and list the 10 most recent hires.
*/
USE EMPLOYEES
DROP VIEW IF EXISTS exercise1_1;

-- Creating view
CREATE VIEW exercise1_1 AS
SELECT
  *
FROM
  EMPLOYEES
WHERE
  YEAR (hire_date) >= 2000;

-- Selecting from view
SELECT
  *
FROM
  exercise1_1;
