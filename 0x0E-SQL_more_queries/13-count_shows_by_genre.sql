-- lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- A genre that doesn’t have any shows linked is not displayed
-- Results are sorted in descending order by the number of shows linked
-- Only one SELECT statement can be used

SELECT tv_genres.name AS 'genre',
COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
