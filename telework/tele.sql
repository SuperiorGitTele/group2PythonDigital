CREATE USER 'tele2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'tele2sql12';
CREATE DATABASE new_data;
GRANT ALL PRIVILEGES ON new_data.* TO 'tele2'@'localhost';
FLUSH PRIVILEGES;