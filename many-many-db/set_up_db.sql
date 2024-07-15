-- Connect to the PostgreSQL instance as a superuser or an existing user with sufficient privileges.
-- Create the database
CREATE DATABASE many_db;

-- Create the user
CREATE ROLE many_user WITH LOGIN PASSWORD 'many_pwd';

-- Grant privileges to the user for the new database
GRANT ALL PRIVILEGES ON DATABASE many_db TO many_user;
