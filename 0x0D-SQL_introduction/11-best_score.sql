-- Lists all scores in a table 'second_table'
-- Only list scores > 10
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
