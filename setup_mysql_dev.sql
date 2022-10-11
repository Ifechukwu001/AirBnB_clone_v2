-- Preparation script for the Airbnb clone database
-- Create a new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user "hbnb_dev" for the database "hbnb_dev_db"
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege to user 'hbnb_dev' on the database performance_schema
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
