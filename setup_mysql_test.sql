-- Preparation script for the Airbnb clone database
-- Create a new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the user hbnb_test for the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to user hbnb_test on the database performance_schema
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';
