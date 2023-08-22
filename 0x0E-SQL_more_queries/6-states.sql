-- Creates a database `hbtn_0d_usa` and a table `states`
-- table has fields `id` and `name`
-- id is a primary key, unique and autogenerated
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(`id` INT AUTO_INCREMENT
	PRIMARY KEY, `name` VARCHAR(256) NOT NULL);