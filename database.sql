-- -----------------------------------------------------
-- Schema tax_db
-- -----------------------------------------------------
USE `tax_db` ;

CREATE TABLE `user` (
	`user_id` varchar(36) NOT NULL,
	`name` varchar(50) NOT NULL,
	`handphone` varchar(13) NOT NULL UNIQUE,
	`password` varchar(40) NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `tax_object` (
	`tax_id` varchar(36) NOT NULL,
	`user_id` varchar(36) NOT NULL,
	`tax_code` enum('1','2','3')  NOT NULL,
	`name` varchar(30) NOT NULL,
	`price` int NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`tax_id`)
);

ALTER TABLE `tax_object` ADD CONSTRAINT `tax_object_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`);
