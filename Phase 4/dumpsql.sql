CREATE DATABASE  IF NOT EXISTS `unsed` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `unsed`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: unsed
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `ambassador`
--

DROP TABLE IF EXISTS `ambassador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ambassador` (
  `Agency_Country` varchar(64) NOT NULL,
  `Agency_Name` varchar(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Nationality` varchar(64) NOT NULL,
  `Contact_Number` varchar(32) DEFAULT NULL,
  `Super_Agency_Country` varchar(64) DEFAULT NULL,
  `Super_Agency_Name` varchar(64) DEFAULT NULL,
  `Super_Name` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`Agency_Country`,`Agency_Name`,`Name`),
  KEY `Super_Agency_Country` (`Super_Agency_Country`,`Super_Agency_Name`,`Super_Name`),
  CONSTRAINT `Ambassador_ibfk_1` FOREIGN KEY (`Super_Agency_Country`, `Super_Agency_Name`, `Super_Name`) REFERENCES `ambassador` (`Agency_Country`, `Agency_Name`, `Name`),
  CONSTRAINT `Ambassador_ibfk_2` FOREIGN KEY (`Agency_Country`, `Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambassador`
--

LOCK TABLES `ambassador` WRITE;
/*!40000 ALTER TABLE `ambassador` DISABLE KEYS */;
INSERT INTO `ambassador` VALUES ('Canada','CSA','Justin Trudeau','Canada','3787242875',NULL,NULL,NULL),('China','CNSA','Yen Li','China','1847134',NULL,NULL,NULL),('Europe','ESA','Jos Verstappen','Netherlands','782387292',NULL,NULL,NULL),('India','ISRO','Narendra Modi','India','9999999999',NULL,NULL,NULL),('India','SkAP','Vineeth Batt','India','3974892849','India','ISRO','Narendra Modi'),('Japan','JAXA','Yuki Tsunoda','Japan','9138374927',NULL,NULL,NULL),('USA','NASA','Raghav Donakanti','USA','1234567890',NULL,NULL,NULL),('USA','SpaceX','Donald Trump','USA','0142847284','USA','NASA','Raghav Donakanti');
/*!40000 ALTER TABLE `ambassador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `astronauts`
--

DROP TABLE IF EXISTS `astronauts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `astronauts` (
  `AstronautID` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `Name` varchar(64) NOT NULL,
  `Nationality` varchar(64) DEFAULT NULL,
  `Mission_Status` varchar(64) NOT NULL,
  PRIMARY KEY (`AstronautID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `astronauts`
--

LOCK TABLES `astronauts` WRITE;
/*!40000 ALTER TABLE `astronauts` DISABLE KEYS */;
INSERT INTO `astronauts` VALUES (0000000001,'Rohan Girish','India','reserve'),(0000000002,'Kimi Raikonnen','Finland','retired'),(0000000003,'Kanye West','USA','on mission'),(0000000004,'Niki MazesBin','Russia','on mission'),(0000000005,'Chris Hadfield','Canada','on mission'),(0000000006,'Jefferey Bezos','USA','on mission');
/*!40000 ALTER TABLE `astronauts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collaboration`
--

DROP TABLE IF EXISTS `collaboration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collaboration` (
  `Mission_Name` varchar(64) NOT NULL,
  `Agency1_Country` varchar(64) NOT NULL,
  `Agency1_Name` varchar(64) NOT NULL,
  `Agency2_Country` varchar(64) NOT NULL,
  `Agency2_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Mission_Name`,`Agency1_Country`,`Agency1_Name`,`Agency2_Country`,`Agency2_Name`),
  KEY `Agency1_Country` (`Agency1_Country`,`Agency1_Name`),
  KEY `Agency2_Country` (`Agency2_Country`,`Agency2_Name`),
  CONSTRAINT `Collaboration_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`) ON DELETE CASCADE,
  CONSTRAINT `Collaboration_ibfk_2` FOREIGN KEY (`Agency1_Country`, `Agency1_Name`) REFERENCES `space_agencies` (`Country`, `Name`),
  CONSTRAINT `Collaboration_ibfk_3` FOREIGN KEY (`Agency2_Country`, `Agency2_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collaboration`
--

LOCK TABLES `collaboration` WRITE;
/*!40000 ALTER TABLE `collaboration` DISABLE KEYS */;
INSERT INTO `collaboration` VALUES ('Challenger','Canada','CSA','USA','NASA'),('ISS','Canada','CSA','USA','NASA'),('ISS','China','CNSA','USA','NASA'),('ISS','Europe','ESA','USA','NASA'),('ISS','Japan','JAXA','USA','NASA'),('Raghav Mission','USA','SpaceX','India','ISRO');
/*!40000 ALTER TABLE `collaboration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract`
--

DROP TABLE IF EXISTS `contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract` (
  `Mission_Name` varchar(64) NOT NULL,
  `AstronautID` int unsigned NOT NULL,
  `Agency_Country` varchar(64) NOT NULL,
  `Agency_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Mission_Name`,`AstronautID`,`Agency_Country`,`Agency_Name`),
  KEY `AstronautID` (`AstronautID`),
  KEY `Agency_Country` (`Agency_Country`,`Agency_Name`),
  CONSTRAINT `Contract_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`) ON DELETE CASCADE,
  CONSTRAINT `Contract_ibfk_2` FOREIGN KEY (`AstronautID`) REFERENCES `astronauts` (`AstronautID`),
  CONSTRAINT `Contract_ibfk_3` FOREIGN KEY (`Agency_Country`, `Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract`
--

LOCK TABLES `contract` WRITE;
/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
INSERT INTO `contract` VALUES ('Apollo 11',1,'USA','NASA'),('Challenger',2,'Europe','ESA'),('Artemis',3,'USA','NASA'),('ISS',4,'Europe','ESA'),('ISS',5,'Canada','CSA');
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeID` varchar(10) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Nationality` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('1111111111','Yeriv Borscj','Romania'),('1234567890','John Doe','USA'),('6562828','Chris Prince','England'),('82378732','Ramez Elmasri','Egypt'),('987654321','Hideo Kojima','Japan');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mission`
--

DROP TABLE IF EXISTS `mission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mission` (
  `Name` varchar(64) NOT NULL,
  `Available_Payload` int DEFAULT NULL,
  `Timeline` varchar(64) NOT NULL,
  `Status` varchar(64) DEFAULT NULL,
  `Open_for_Collaboration` tinyint(1) DEFAULT NULL,
  `Astronauts_Required` tinyint(1) DEFAULT NULL,
  `Purpose` varchar(256) NOT NULL,
  `Celestial_Body` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mission`
--

LOCK TABLES `mission` WRITE;
/*!40000 ALTER TABLE `mission` DISABLE KEYS */;
INSERT INTO `mission` VALUES ('Apollo 11',0,'Past','Successful',0,0,'Men on the moon','Moon'),('APS',98761,'Future',NULL,1,0,'Probe Mars','Mars'),('Artemis',0,'In Progress',NULL,0,0,'People on the moon again','Moon'),('Challenger',18964,'Past','Failed',1,5,'Trip to the ISS','Earth'),('ISS',928387482,'In Progress',NULL,1,6,'Experiments in Space','Earth'),('Raghav Mission',121311,'Future','Scrapped',1,1,'Find intelligence','Mars');
/*!40000 ALTER TABLE `mission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mission_agencies`
--

DROP TABLE IF EXISTS `mission_agencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mission_agencies` (
  `Name` varchar(64) NOT NULL,
  `Agency_Country` varchar(64) NOT NULL,
  `Agency_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Name`,`Agency_Country`,`Agency_Name`),
  KEY `Agency_Country` (`Agency_Country`,`Agency_Name`),
  CONSTRAINT `Mission_Agencies_ibfk_1` FOREIGN KEY (`Name`) REFERENCES `mission` (`Name`),
  CONSTRAINT `Mission_Agencies_ibfk_2` FOREIGN KEY (`Agency_Country`, `Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mission_agencies`
--

LOCK TABLES `mission_agencies` WRITE;
/*!40000 ALTER TABLE `mission_agencies` DISABLE KEYS */;
INSERT INTO `mission_agencies` VALUES ('Challenger','Canada','CSA'),('ISS','Canada','CSA'),('ISS','China','CNSA'),('ISS','Europe','ESA'),('Raghav Mission','India','ISRO'),('ISS','Japan','JAXA'),('Apollo 11','USA','NASA'),('Artemis','USA','NASA'),('Challenger','USA','NASA'),('ISS','USA','NASA'),('Raghav Mission','USA','SpaceX');
/*!40000 ALTER TABLE `mission_agencies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mission_rockets`
--

DROP TABLE IF EXISTS `mission_rockets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mission_rockets` (
  `Mission_Name` varchar(64) NOT NULL,
  `Rocket_Model` varchar(64) NOT NULL,
  `Rocket_Agency_Country` varchar(64) NOT NULL,
  `Rocket_Agency_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Mission_Name`,`Rocket_Model`,`Rocket_Agency_Country`,`Rocket_Agency_Name`),
  KEY `Rocket_Model` (`Rocket_Model`,`Rocket_Agency_Country`,`Rocket_Agency_Name`),
  CONSTRAINT `Mission_Rockets_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`),
  CONSTRAINT `Mission_Rockets_ibfk_2` FOREIGN KEY (`Rocket_Model`, `Rocket_Agency_Country`, `Rocket_Agency_Name`) REFERENCES `rocket` (`Model_Name`, `Agency_Country`, `Agency_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mission_rockets`
--

LOCK TABLES `mission_rockets` WRITE;
/*!40000 ALTER TABLE `mission_rockets` DISABLE KEYS */;
INSERT INTO `mission_rockets` VALUES ('Raghav Mission','Falcon Heavy','USA','SpaceX'),('Raghav Mission','PSLV','India','ISRO'),('Artemis','SLS','USA','NASA');
/*!40000 ALTER TABLE `mission_rockets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payload`
--

DROP TABLE IF EXISTS `payload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payload` (
  `Mission_Name` varchar(64) NOT NULL,
  `Experiment_Name` varchar(64) NOT NULL,
  `Weight` int NOT NULL,
  `Sender_Country` varchar(64) NOT NULL,
  `Sender_Name` varchar(64) NOT NULL,
  `Rocket_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Mission_Name`,`Experiment_Name`),
  KEY `Sender_Country` (`Sender_Country`,`Sender_Name`),
  KEY `Rocket_Name` (`Rocket_Name`),
  CONSTRAINT `Payload_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`),
  CONSTRAINT `Payload_ibfk_2` FOREIGN KEY (`Sender_Country`, `Sender_Name`) REFERENCES `space_agencies` (`Country`, `Name`),
  CONSTRAINT `Payload_ibfk_3` FOREIGN KEY (`Rocket_Name`) REFERENCES `rocket` (`Model_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payload`
--

LOCK TABLES `payload` WRITE;
/*!40000 ALTER TABLE `payload` DISABLE KEYS */;
INSERT INTO `payload` VALUES ('Artemis','Soil Analysis',400,'USA','NASA','SLS'),('Challenger','Heat Shield Test',350,'Canada','CSA','SLS'),('ISS','Effects of Anti-Gravity',600,'India','ISRO','Falcon Heavy'),('Raghav Mission','Intelligence Detection',200,'USA','SpaceX','Falcon Heavy');
/*!40000 ALTER TABLE `payload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource_request`
--

DROP TABLE IF EXISTS `resource_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resource_request` (
  `Mission_Name` varchar(64) NOT NULL,
  `Resource_Name` varchar(64) NOT NULL,
  `Ambassador1_Agency_Country` varchar(64) NOT NULL,
  `Ambassador1_Agency_Name` varchar(64) NOT NULL,
  `Ambassador1_Name` varchar(64) NOT NULL,
  `Ambassador2_Agency_Country` varchar(64) NOT NULL,
  `Ambassador2_Agency_Name` varchar(64) NOT NULL,
  `Ambassador2_Name` varchar(64) NOT NULL,
  `EmployeeID` varchar(10) NOT NULL,
  `Agency_Country` varchar(64) NOT NULL,
  `Agency_Name` varchar(64) NOT NULL,
  PRIMARY KEY (`Mission_Name`,`Resource_Name`,`Ambassador1_Agency_Name`,`Ambassador1_Name`,`Ambassador2_Agency_Country`,`Ambassador2_Agency_Name`,`Ambassador2_Name`,`EmployeeID`,`Agency_Country`,`Agency_Name`),
  KEY `Ambassador1_Agency_Country` (`Ambassador1_Agency_Country`,`Ambassador1_Agency_Name`,`Ambassador1_Name`),
  KEY `Ambassador2_Agency_Country` (`Ambassador2_Agency_Country`,`Ambassador2_Agency_Name`,`Ambassador2_Name`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `Agency_Country` (`Agency_Country`,`Agency_Name`),
  CONSTRAINT `Resource_Request_ibfk_1` FOREIGN KEY (`Mission_Name`, `Resource_Name`) REFERENCES `resources` (`Mission_Name`, `Resource_Name`),
  CONSTRAINT `Resource_Request_ibfk_2` FOREIGN KEY (`Ambassador1_Agency_Country`, `Ambassador1_Agency_Name`, `Ambassador1_Name`) REFERENCES `ambassador` (`Agency_Country`, `Agency_Name`, `Name`),
  CONSTRAINT `Resource_Request_ibfk_3` FOREIGN KEY (`Ambassador2_Agency_Country`, `Ambassador2_Agency_Name`, `Ambassador2_Name`) REFERENCES `ambassador` (`Agency_Country`, `Agency_Name`, `Name`),
  CONSTRAINT `Resource_Request_ibfk_4` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`),
  CONSTRAINT `Resource_Request_ibfk_5` FOREIGN KEY (`Agency_Country`, `Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource_request`
--

LOCK TABLES `resource_request` WRITE;
/*!40000 ALTER TABLE `resource_request` DISABLE KEYS */;
INSERT INTO `resource_request` VALUES ('ISS','Medical Equipment','Europe','ESA','Jos Verstappen','USA','NASA','Raghav Donakanti','6562828','USA','NASA'),('ISS','Exercise Equipment','Japan','JAXA','Yuki Tsunoda','Canada','CSA','Justin Trudeau','82378732','USA','NASA'),('Artemis','Oxygen','USA','NASA','Raghav Donakanti','Europe','ESA','Jos Verstappen','1111111111','USA','NASA'),('Raghav Mission','Raghavs','USA','SpaceX','Donald Trump','India','ISRO','Narendra Modi','1234567890','USA','SpaceX');
/*!40000 ALTER TABLE `resource_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources`
--

DROP TABLE IF EXISTS `resources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resources` (
  `Mission_Name` varchar(64) NOT NULL,
  `Resource_Name` varchar(64) NOT NULL,
  `Quantity` int DEFAULT NULL,
  `Requesting_Agency_Country` varchar(64) NOT NULL,
  `Requesting_Agency_Name` varchar(64) NOT NULL,
  `Country_Requested_From` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`Mission_Name`,`Resource_Name`),
  KEY `Requesting_Agency_Country` (`Requesting_Agency_Country`,`Requesting_Agency_Name`),
  CONSTRAINT `Resources_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`),
  CONSTRAINT `Resources_ibfk_2` FOREIGN KEY (`Requesting_Agency_Country`, `Requesting_Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources`
--

LOCK TABLES `resources` WRITE;
/*!40000 ALTER TABLE `resources` DISABLE KEYS */;
INSERT INTO `resources` VALUES ('Artemis','Oxygen',5000,'USA','NASA','UK'),('ISS','Exercise Equipment',10,'Japan','JAXA','Canada'),('ISS','Medical Equipment',50,'Europe','ESA','USA'),('ISS','Solar Panels',32,'Canada','CSA','USA'),('Raghav Mission','Raghavs',3,'USA','SpaceX','India');
/*!40000 ALTER TABLE `resources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rocket`
--

DROP TABLE IF EXISTS `rocket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rocket` (
  `Model_Name` varchar(64) NOT NULL,
  `Agency_Country` varchar(64) NOT NULL,
  `Agency_Name` varchar(64) NOT NULL,
  `Max_Payload` int DEFAULT NULL,
  `Fuel_Type` varchar(64) DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  `Year_First_Use` date DEFAULT NULL,
  `Engines` varchar(128) DEFAULT NULL,
  `Status` varchar(64) DEFAULT NULL,
  `Fuel_Efficiency` decimal(5,2) DEFAULT NULL,
  `Reusable` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Model_Name`,`Agency_Country`,`Agency_Name`),
  KEY `Agency_Country` (`Agency_Country`,`Agency_Name`),
  CONSTRAINT `Rocket_ibfk_1` FOREIGN KEY (`Agency_Country`, `Agency_Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rocket`
--

LOCK TABLES `rocket` WRITE;
/*!40000 ALTER TABLE `rocket` DISABLE KEYS */;
INSERT INTO `rocket` VALUES ('Falcon Heavy','USA','SpaceX',16800,'Chilled RP-1',97000000,'2018-01-20','Merlin 1D','in use',88.00,1),('Prometheus','Europe','ESA',18000,'Methane',NULL,'2022-11-18','Prometheus','in use',94.00,1),('PSLV','India','ISRO',20000,'N2O4',2000000,'1993-09-19','S139','in use',90.00,0),('SLS','USA','NASA',50000,'SLSF',127000000,'1969-07-16','SLS','in use',85.00,0);
/*!40000 ALTER TABLE `rocket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `space_agencies`
--

DROP TABLE IF EXISTS `space_agencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `space_agencies` (
  `Country` varchar(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Public` tinyint(1) NOT NULL,
  `EmpNo` int DEFAULT '0',
  PRIMARY KEY (`Country`,`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `space_agencies`
--

LOCK TABLES `space_agencies` WRITE;
/*!40000 ALTER TABLE `space_agencies` DISABLE KEYS */;
INSERT INTO `space_agencies` VALUES ('Canada','CSA',1,NULL),('China','CNSA',1,NULL),('Europe','ESA',1,2200),('India','ISRO',1,16500),('India','SkAP',0,8620),('Japan','JAXA',1,1500),('Russia','ROSCOSMOS',1,14718),('USA','NASA',1,18000),('USA','SpaceX',0,7000);
/*!40000 ALTER TABLE `space_agencies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `space_agency_locations`
--

DROP TABLE IF EXISTS `space_agency_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `space_agency_locations` (
  `Country` varchar(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `Location` varchar(128) NOT NULL,
  PRIMARY KEY (`Country`,`Name`,`Location`),
  CONSTRAINT `Space_Agency_Locations_ibfk_1` FOREIGN KEY (`Country`, `Name`) REFERENCES `space_agencies` (`Country`, `Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `space_agency_locations`
--

LOCK TABLES `space_agency_locations` WRITE;
/*!40000 ALTER TABLE `space_agency_locations` DISABLE KEYS */;
INSERT INTO `space_agency_locations` VALUES ('Canada','CSA','Ontario'),('Canada','CSA','Quebec'),('China','CNSA','Beijing'),('Europe','ESA','Paris'),('India','ISRO','Bengaluru'),('India','ISRO','Sriharikota'),('India','SkAP','Chennai'),('Japan','JAXA','Tokyo'),('USA','NASA','Washington D.C.'),('USA','SpaceX','Redmond');
/*!40000 ALTER TABLE `space_agency_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travelled_on`
--

DROP TABLE IF EXISTS `travelled_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travelled_on` (
  `Mission_Name` varchar(64) NOT NULL,
  `Rocket_Model` varchar(64) NOT NULL,
  `Rocket_Agency_Country` varchar(64) NOT NULL,
  `Rocket_Agency_Name` varchar(64) NOT NULL,
  `AstronautID` int unsigned NOT NULL,
  PRIMARY KEY (`Mission_Name`,`Rocket_Model`,`Rocket_Agency_Country`,`Rocket_Agency_Name`,`AstronautID`),
  KEY `Rocket_Agency_Country` (`Rocket_Agency_Country`,`Rocket_Agency_Name`,`Rocket_Model`),
  KEY `AstronautID` (`AstronautID`),
  CONSTRAINT `Travelled_On_ibfk_1` FOREIGN KEY (`Mission_Name`) REFERENCES `mission` (`Name`),
  CONSTRAINT `Travelled_On_ibfk_2` FOREIGN KEY (`Rocket_Agency_Country`, `Rocket_Agency_Name`, `Rocket_Model`) REFERENCES `rocket` (`Agency_Country`, `Agency_Name`, `Model_Name`),
  CONSTRAINT `Travelled_On_ibfk_3` FOREIGN KEY (`AstronautID`) REFERENCES `astronauts` (`AstronautID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travelled_on`
--

LOCK TABLES `travelled_on` WRITE;
/*!40000 ALTER TABLE `travelled_on` DISABLE KEYS */;
INSERT INTO `travelled_on` VALUES ('Apollo 11','SLS','USA','NASA',1),('Artemis','SLS','USA','NASA',3),('ISS','Prometheus','Europe','ESA',4),('ISS','Prometheus','Europe','ESA',5),('ISS','SLS','USA','NASA',6);
/*!40000 ALTER TABLE `travelled_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 21:47:36
