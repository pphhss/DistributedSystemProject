
SET GLOBAL validate_password_policy=LOW;
SET GLOBAL validate_password_length =4;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';



CREATE DATABASE ds DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use ds;
CREATE TABLE data(
	idx int(1) not null AUTO_INCREMENT,
	data varchar(20),
	PRIMARY KEY(idx)
);
