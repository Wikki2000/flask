-- Create the database
CREATE DATABASE IF NOT EXISTS test_db;

-- Create the user
CREATE USER IF NOT EXISTS 'test_user'@'localhost' IDENTIFIED BY 'test_pwd';

-- Grant all privileges on the test_db database to the test_user
GRANT ALL PRIVILEGES ON test_db.* TO 'test_user'@'localhost';

-- Flush the privileges to ensure they are saved and available in the current session
FLUSH PRIVILEGES;

