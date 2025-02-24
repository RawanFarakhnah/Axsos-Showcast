CREATE DATABASE  IF NOT EXISTS `martion_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `martion_database`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: martion_database
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bases`
--

DROP TABLE IF EXISTS `bases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `base_name` varchar(255) NOT NULL,
  `founded` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bases`
--

LOCK TABLES `bases` WRITE;
/*!40000 ALTER TABLE `bases` DISABLE KEYS */;
INSERT INTO `bases` VALUES (1,'Tharsisland','2025-02-23 13:25:46'),(2,'Valles Marineris 2.0','2025-02-23 13:25:46'),(3,'Gale Cratertown','2025-02-23 13:25:46'),(4,'New New New York','2025-02-23 13:25:46'),(5,'Olympus Mons Spa & Casino',NULL);
/*!40000 ALTER TABLE `bases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventories`
--

DROP TABLE IF EXISTS `inventories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `base_id` int DEFAULT NULL,
  `supply_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_id` (`base_id`),
  KEY `supply_id` (`supply_id`),
  CONSTRAINT `inventories_ibfk_1` FOREIGN KEY (`base_id`) REFERENCES `bases` (`id`),
  CONSTRAINT `inventories_ibfk_2` FOREIGN KEY (`supply_id`) REFERENCES `supplies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventories`
--

LOCK TABLES `inventories` WRITE;
/*!40000 ALTER TABLE `inventories` DISABLE KEYS */;
INSERT INTO `inventories` VALUES (1,8,1,1),(2,5,1,3),(3,1,1,5),(4,2,1,6),(5,12,1,8),(6,1,1,9),(7,5,2,4),(8,62,2,8),(9,37,2,10),(10,11,3,3),(11,2,3,7),(12,91,4,10);
/*!40000 ALTER TABLE `inventories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `martians`
--

DROP TABLE IF EXISTS `martians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `martians` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `base_id` int DEFAULT NULL,
  `super_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_id` (`base_id`),
  KEY `super_id` (`super_id`),
  CONSTRAINT `martians_ibfk_1` FOREIGN KEY (`base_id`) REFERENCES `bases` (`id`),
  CONSTRAINT `super_id` FOREIGN KEY (`super_id`) REFERENCES `martians` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `martians`
--

LOCK TABLES `martians` WRITE;
/*!40000 ALTER TABLE `martians` DISABLE KEYS */;
INSERT INTO `martians` VALUES (1,'Ray','Bradbury',1,NULL),(2,'John','Black',4,10),(3,'Samuel','Hinkston',4,2),(4,'Jeff','Spender',1,9),(5,'Sam','Parkhill',2,12),(6,'Elma','Parkhill',3,8),(7,'Melissa','Lewis',1,1),(8,'Mark','Watney',3,NULL),(9,'Beth','Johanssen',1,1),(10,'Chris','Beck',4,NULL),(11,'Nathaniel','York',4,2),(12,'Elon','Musk',2,NULL),(13,'John','Carter',NULL,8);
/*!40000 ALTER TABLE `martians` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplies`
--

DROP TABLE IF EXISTS `supplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplies`
--

LOCK TABLES `supplies` WRITE;
/*!40000 ALTER TABLE `supplies` DISABLE KEYS */;
INSERT INTO `supplies` VALUES (1,'Oxygen Tanks','Portable oxygen tanks for breathing support',50),(2,'Food Rations','Dehydrated food packs for survival',200),(3,'Water Containers','Large sealed containers of purified water',100),(4,'Space Suits','Protective suits for external Mars operations',10),(5,'Solar Panels','Energy source for Martian base operations',25),(6,'Medical Kits','Emergency medical kits with basic supplies',30),(7,'Communication Devices','Handheld radios for internal communication',15),(8,'Batteries','Rechargeable batteries for electronic devices',75),(9,'Tools Set','Basic tools for equipment maintenance',20),(10,'Rover Parts','Spare parts for repairing exploration rovers',40);
/*!40000 ALTER TABLE `supplies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visitors`
--

DROP TABLE IF EXISTS `visitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `host_id` int DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `host_id` (`host_id`),
  CONSTRAINT `visitors_ibfk_1` FOREIGN KEY (`host_id`) REFERENCES `martians` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitors`
--

LOCK TABLES `visitors` WRITE;
/*!40000 ALTER TABLE `visitors` DISABLE KEYS */;
INSERT INTO `visitors` VALUES (1,7,'George','Ambrose'),(2,1,'Kris','Cardenas'),(3,9,'Priscilla','Lane'),(4,11,'Jane','Thornton'),(5,NULL,'Doug','Stavenger'),(6,NULL,'Jamie','Waterman'),(7,8,'Martin','Humphries');
/*!40000 ALTER TABLE `visitors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-23 22:57:35
