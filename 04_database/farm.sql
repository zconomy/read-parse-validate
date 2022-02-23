DROP DATABASE IF EXISTS `Farm`;
CREATE DATABASE IF NOT EXISTS `Farm`;
USE `Farm`;

CREATE TABLE `Customers` (
    `FirstName` varchar(20) NULL,
    `lastName` varchar(20) NULL,
    `Email` varchar(30) NULL
);

INSERT INTO `Customers` VALUES
    ('kaka', 'ka' , 'ka@mit.edu'),
    ('kakaka', 'laa' , 'laa@mit.edu');