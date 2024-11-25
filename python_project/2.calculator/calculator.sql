-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: CALCULATOR
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ADDITION`
--

DROP TABLE IF EXISTS `ADDITION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ADDITION` (
  `A` int DEFAULT NULL,
  `B` int DEFAULT NULL,
  `RESULT` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADDITION`
--

LOCK TABLES `ADDITION` WRITE;
/*!40000 ALTER TABLE `ADDITION` DISABLE KEYS */;
INSERT INTO `ADDITION` VALUES (10,20,30),(11,12,23);
/*!40000 ALTER TABLE `ADDITION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIVISION`
--

DROP TABLE IF EXISTS `DIVISION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DIVISION` (
  `A` int DEFAULT NULL,
  `B` int DEFAULT NULL,
  `RESULT` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIVISION`
--

LOCK TABLES `DIVISION` WRITE;
/*!40000 ALTER TABLE `DIVISION` DISABLE KEYS */;
INSERT INTO `DIVISION` VALUES (3,2,2);
/*!40000 ALTER TABLE `DIVISION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MULTIPLICATION`
--

DROP TABLE IF EXISTS `MULTIPLICATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MULTIPLICATION` (
  `A` int DEFAULT NULL,
  `B` int DEFAULT NULL,
  `RESULT` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MULTIPLICATION`
--

LOCK TABLES `MULTIPLICATION` WRITE;
/*!40000 ALTER TABLE `MULTIPLICATION` DISABLE KEYS */;
INSERT INTO `MULTIPLICATION` VALUES (5,5,25),(55,56,3080);
/*!40000 ALTER TABLE `MULTIPLICATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBTRACTION`
--

DROP TABLE IF EXISTS `SUBTRACTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBTRACTION` (
  `A` int DEFAULT NULL,
  `B` int DEFAULT NULL,
  `RESULT` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBTRACTION`
--

LOCK TABLES `SUBTRACTION` WRITE;
/*!40000 ALTER TABLE `SUBTRACTION` DISABLE KEYS */;
INSERT INTO `SUBTRACTION` VALUES (25,30,-5),(10,10,0);
/*!40000 ALTER TABLE `SUBTRACTION` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-25 16:09:16