-- Create a new user if doesn't exist and grant all privileges --
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
