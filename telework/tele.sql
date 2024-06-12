CREATE USER 'tele'@'localhost' IDENTIFIED WITH mysql_native_password BY 'telesql19';
CREATE DATABASE new_database;
GRANT ALL PRIVILEGES ON new_database.* TO 'tele'@'localhost';
FLUSH PRIVILEGES;