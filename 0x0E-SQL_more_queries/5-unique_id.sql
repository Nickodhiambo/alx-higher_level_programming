-- Creates a table `unique_id`
-- sets its id and name fields
-- Id's default value is 1 and every id should be unique
CREATE TABLE IF NOT EXISTS `unique_id`(`id` INT DEFAULT 1 UNIQUE,
	                              `name` VARCHAR(256));
