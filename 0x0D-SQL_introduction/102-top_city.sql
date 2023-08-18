-- Imports the file 'temperatures.sql into database
-- Finds the average temp of cities for July and August
-- Groups avg temps in descending order

SELECT city, AVG(value) AS avg_temp
FROM `temperatures`
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
