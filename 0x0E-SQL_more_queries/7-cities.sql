-- Creates a table `cities` in the database `hbtn_0d_usa`
-- Table has fields `id` and `name` containing ids and names of cities
-- Cities table references state ids in a table `states`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT
	PRIMARY KEY, state_id INT, FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL);
