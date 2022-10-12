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
  `goals` int NOT NULL COMMENT 'credits used on this bet',
  `user_id` binary(16) NOT NULL COMMENT 'the id of the user that made this bet',
  `status` varchar(100) NOT NULL COMMENT 'the status of the bet',
  `result` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'resultado del evento (l: local, e:empate, v:visita)',
  `event_id` binary(16) NOT NULL COMMENT 'el id del evento para esta apuesta',
  PRIMARY KEY (`id`),
  KEY `bet_user_id_FK` (`user_id`),
  KEY `bet_FK` (`event_id`),
  CONSTRAINT `bet_FK` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`),
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
  `event_end` datetime NOT NULL COMMENT 'fecha y hora de finalizacion del evento',
  `stats_link` text NOT NULL COMMENT 'link a website con estadisticas (como sportsradar)',
  `goals` int DEFAULT NULL COMMENT 'cantidad de goles del ganador o del empate',
  `result` char(1) DEFAULT NULL COMMENT 'l: local, e: empate, v:visita',
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
INSERT INTO `event` VALUES (_binary '½\Þ2>JFí•ª\0]1e','2020-08-01 08:50:00',_binary '\'\æ0JJ4\í›\Ù\0]1e',_binary '\ð\Úm\ÖJ4\í˜ù\0]1e',_binary '…Cn\ÒJ5\í»\Ã\0]1e','2020-08-01 08:50:00','https://s5.sir.sportradar.com/intralotchile/es/1/season/90425/h2h/6092/706/match/31672715',1,'l');
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
INSERT INTO `event_category` VALUES (_binary '\ì¨ý¼J5\í¸²\0]1e','Primera Division Argentina'),(_binary '…Cn\ÒJ5\í»\Ã\0]1e','Primera Division Chile');
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
INSERT INTO `event_player` VALUES (_binary '\Ì\ã†\öJ4\í˜\0]1e','Cobreloa'),(_binary '\ð\Úm\ÖJ4\í˜ù\0]1e','Cobresal'),(_binary '\'\æ0JJ4\í›\Ù\0]1e','Colo Colo'),(_binary '\Ø\àBZJ4\íšk\0]1e','Huachipato'),(_binary '\Ø\Ü\×J3\í”M\0]1e','U. Catolica'),(_binary 'Ä†VJ3\í¦\Õ\0]1e','U. de Chile'),(_binary 'dºÙžJ4í†Ÿ\0]1e','Union EspaÃ±ola');
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
INSERT INTO `user` VALUES (_binary '	œLE}\í‘I\0]#2','r1@r.com','r1','123','jugador',NULL),(_binary '—OJK\í½&\0]1e','r7@r.com','r1','123','jugador',NULL),(_binary '›P\ÜJK\í€q\0]1e','r8@r.com','r1','123','jugador',NULL),(_binary '\Ê\Ý@\nJL\í¼¤\0]1e','r9@r.com','r1','123','jugador',NULL),(_binary '\ó\óIv\íº\0]SS','r3@r.com','r1','12345','jugador',NULL),(_binary '\ón82D\ï\í¥\0]#2','r@r.com','r','123','jugador',NULL),(_binary 'þ5^Iu\í˜\ê\0]SS','r2@r.com','r1','123','jugador',NULL);
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

-- Dump completed on 2022-10-12 13:56:12
