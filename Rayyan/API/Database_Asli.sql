-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.27-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for store
CREATE DATABASE IF NOT EXISTS `store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `store`;

-- Dumping structure for table store.address_store
CREATE TABLE IF NOT EXISTS `address_store` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `postal_code` int(7) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_address_store_customer_store` (`customer_id`),
  CONSTRAINT `FK_address_store_customer_store` FOREIGN KEY (`customer_id`) REFERENCES `customer_store` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table store.address_store: ~2 rows (approximately)
INSERT IGNORE INTO `address_store` (`id`, `customer_id`, `address`, `district`, `city`, `province`, `postal_code`, `created_at`, `updated_at`) VALUES
	(1, 1, 'Kawasan Karyadeka Pancamurni Y', 'Kopo1', 'Bandung', 'Jawa Barat', 40228, '2020-08-01 10:56:31', '2020-08-08 09:30:23');

-- Dumping structure for table store.customer_store
CREATE TABLE IF NOT EXISTS `customer_store` (
  `id` int(11) NOT NULL,
  `title` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `gender` varchar(3) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table store.customer_store: ~8 rows (approximately)
INSERT IGNORE INTO `customer_store` (`id`, `title`, `name`, `gender`, `phone_number`, `image`, `email`, `created_at`, `updated_at`) VALUES
	(1, 'Ms', 'Adrien Philippe Ramo1', 'FPS', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(2, 'Ms', 'Badrien Philippe Ramoz', 'FFS', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(3, 'Ms', 'Adrien Philippe Ramos 3', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(4, 'Ms', 'Adrien Philippe Ramos 4', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(5, 'Ms', 'Adrien Philippe Ramos 5', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(6, 'Ms', 'Adrien Philippe Ramos 6', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(7, 'Ms', 'Adrien Philippe Ramos 7', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23'),
	(8, 'Ms', 'Adrien Philippe Ramos 8', 'M', '085222334445', 'https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg', 'adrien.philippe@gmail.com', '2020-08-01 10:56:31', '2020-08-08 09:30:23');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
