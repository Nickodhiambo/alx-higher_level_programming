-- Displays average temperature(Fahrenheit)
-- based on data from American cities
-- Displays data by temp in descending order
SELECT city, AVG(value) AS avg_temp FROM `temperatures`
GROUP BY city ORDER BY avg_temp DESC;
