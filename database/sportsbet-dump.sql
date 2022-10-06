-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: sportbet
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

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
-- Table structure for table `bet`
--

DROP TABLE IF EXISTS `bet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bet` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())),
  `bet_datetime` datetime NOT NULL COMMENT 'date and time of the bet',
  `bet_amount` decimal(10,4) NOT NULL COMMENT 'credits used on this bet',
  `user_id` binary(16) NOT NULL COMMENT 'the id of the user that made this bet',
  `status` varchar(100) NOT NULL COMMENT 'the status of the bet',
  PRIMARY KEY (`id`),
  KEY `bet_user_id_FK` (`user_id`),
  CONSTRAINT `bet_user_id_FK` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bet`
--

LOCK TABLES `bet` WRITE;
/*!40000 ALTER TABLE `bet` DISABLE KEYS */;
/*!40000 ALTER TABLE `bet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bet_event`
--

DROP TABLE IF EXISTS `bet_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bet_event` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())) COMMENT 'referencia',
  `event_id` binary(16) NOT NULL COMMENT 'referencia al id del evento',
  `bet_id` binary(16) NOT NULL COMMENT 'id of the event type',
  `bet_name` varchar(3) NOT NULL COMMENT 'nombre de la apuesta ejemplo: rfl (resultado final local)',
  `bet_factor` decimal(6,4) NOT NULL COMMENT 'el factor de la apuesta al momento de crearla',
  PRIMARY KEY (`id`),
  KEY `bet_event_event_id_FK` (`event_id`),
  KEY `bet_event_bet_id_FK` (`bet_id`),
  CONSTRAINT `bet_event_bet_id_FK` FOREIGN KEY (`bet_id`) REFERENCES `bet` (`id`),
  CONSTRAINT `bet_event_event_id_FK` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='apuestas hechas por usuarios a eventos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bet_event`
--

LOCK TABLES `bet_event` WRITE;
/*!40000 ALTER TABLE `bet_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `bet_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())) COMMENT '36 caracteres (32 hex digits + 4 dashes), se usa para referenciar registro',
  `event_start` datetime NOT NULL COMMENT 'fecha y hora de comienzo del evento',
  `local_player` binary(16) NOT NULL COMMENT 'equipo o jugador local',
  `visitor_player` binary(16) NOT NULL COMMENT 'equipo o jugador visitante',
  `category` binary(16) NOT NULL COMMENT 'categoria del evento',
  `rfl` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a resultado final local',
  `rfv` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a resultado final visitante',
  `rfe` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a resultado final empate',
  `ptl` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a primer tiempo local',
  `ptv` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a primer tiempo visitante',
  `gv0` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a gol visitante = 0',
  `gv1` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a gol visitante = 1',
  `gv2` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a gol visitante = 2',
  `gv3` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a gol visitante = 3',
  `pte` decimal(6,4) NOT NULL DEFAULT '0.0000' COMMENT 'factor de pago a primer tiempo empate',
  `event_end` datetime NOT NULL COMMENT 'fecha y hora de finalizacion del evento',
  `minimum_bets` int NOT NULL DEFAULT '1' COMMENT 'minima cantidad de apuestas para este evento',
  `stats_link` text NOT NULL COMMENT 'link a website con estadisticas (como sportsradar)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_UN` (`event_start`,`local_player`,`visitor_player`,`category`),
  KEY `event_category_FK` (`category`),
  KEY `event_local_player_FK` (`local_player`),
  KEY `event_visitor_player_FK` (`visitor_player`),
  CONSTRAINT `event_category_FK` FOREIGN KEY (`category`) REFERENCES `event_category` (`id`),
  CONSTRAINT `event_local_player_FK` FOREIGN KEY (`local_player`) REFERENCES `event_player` (`id`),
  CONSTRAINT `event_visitor_player_FK` FOREIGN KEY (`visitor_player`) REFERENCES `event_player` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='eventos sobre los cuales se puede apostar';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_category`
--

DROP TABLE IF EXISTS `event_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_category` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())) COMMENT '36 caracteres (32 hex digits + 4 dashes), se usa para referenciar registro',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'nombre de la categoria de un evento',
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_UN` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='categorias de eventos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_category`
--

LOCK TABLES `event_category` WRITE;
/*!40000 ALTER TABLE `event_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_player`
--

DROP TABLE IF EXISTS `event_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_player` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())) COMMENT '36 caracteres (32 hex digits + 4 dashes), se usa para referenciar registro',
  `name` varchar(100) NOT NULL COMMENT 'nombre del equipo o jugador de un evento',
  PRIMARY KEY (`id`),
  UNIQUE KEY `player_UN` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='equipo o jugadores en eventos  (no son usuarios)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_player`
--

LOCK TABLES `event_player` WRITE;
/*!40000 ALTER TABLE `event_player` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` binary(16) NOT NULL DEFAULT (uuid_to_bin(uuid())),
  `email` varchar(100) NOT NULL COMMENT 'correo electronico',
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'apodo que el usuario elige',
  `credit` decimal(10,10) NOT NULL DEFAULT '0.0000000000' COMMENT 'credito del usuario para jugar',
  `md5` varchar(100) NOT NULL COMMENT 'password md5',
  `role` varchar(10) NOT NULL DEFAULT 'jugador' COMMENT 'indica el rol del usuario entre: jugador o admin',
  `login_uuid` binary(16) DEFAULT NULL COMMENT 'the uuid for a logged in user',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='usuarios del sistema';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (_binary '\ón82D\ï\í¥\0]#2','r@r.com','r',0.0000000000,'123','jugador',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-05 20:17:22
