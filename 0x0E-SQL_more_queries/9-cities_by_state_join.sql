-- Lists all cities in the database `hbtn_0d_usa`
-- The record displays city id, city name and state name
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
