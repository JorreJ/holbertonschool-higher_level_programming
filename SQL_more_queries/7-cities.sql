-- create a database 'hbtn_0d_usa' and a table 'cities'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
    state_id INT NOT NULL
	name VARCHAR(256)
    FOREIGN KEY(state_id) REFERENCES states(id)
);
