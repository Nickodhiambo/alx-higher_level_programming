-- Lists the number of records with the same score
-- from table 'second_table'
-- Displays the score with the number of records
-- for the score
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
