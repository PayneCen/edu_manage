-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: edu_manage
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `a_id` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `tel` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `birth` varchar(255) NOT NULL,
  `aname` varchar(255) NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('10001','123','男','10086','1@bucea.a.com','-259/01/27','秦始皇'),('10002','123','女','10010','2@bucea.a.com','0624/12/16','武则天'),('10003','123','男','10011','3@bucea.a.com','1152/08/25','成吉思汗'),('a1','123','男','12312','4@bucea.a.com','1000/01/01','test admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choose`
--

DROP TABLE IF EXISTS `choose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `choose` (
  `c_sno` varchar(255) NOT NULL,
  `c_cno` varchar(255) NOT NULL,
  `score` int DEFAULT NULL,
  PRIMARY KEY (`c_sno`,`c_cno`),
  KEY `Choose_course_cno_fk` (`c_cno`),
  CONSTRAINT `Choose_student_sno_fk` FOREIGN KEY (`c_sno`) REFERENCES `student` (`sno`),
  CONSTRAINT `ck_grade` CHECK (((`score` >= 0) and (`score` <= 100)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choose`
--

LOCK TABLES `choose` WRITE;
/*!40000 ALTER TABLE `choose` DISABLE KEYS */;
INSERT INTO `choose` VALUES ('201807010114','1',NULL),('201807010114','22',NULL),('201807010114','25',NULL),('201807010114','28',NULL),('201807010116','21',NULL),('201807010116','23',51),('201807010116','25',51),('201807010116','26',51),('201807010116','27',51),('201807010116','29',100),('201807010123','1',NULL),('201807010123','20',NULL),('201807010123','24',NULL),('201807010123','25',NULL),('201807010123','26',NULL),('201807010123','27',NULL),('201807010123','28',NULL),('201807010124','20',80),('201807010124','21',70),('201807010124','22',60),('201807010124','23',NULL),('201807010124','24',NULL),('201807010124','25',NULL),('201807010124','27',NULL),('201807010124','28',NULL),('201807010124','29',NULL),('201807010124','30',NULL),('201807010127','1',100),('201807010127','20',NULL),('201807010127','21',NULL),('201807010127','22',NULL),('201807010127','23',51),('201807010127','24',NULL),('201807010127','25',NULL),('201807010127','26',85),('201807010127','27',NULL),('201807010127','28',NULL),('201807010127','29',59),('201807010127','30',NULL);
/*!40000 ALTER TABLE `choose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `cid` varchar(255) NOT NULL,
  `major` varchar(255) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES ('1','信息与计算科学'),('2','城市管理'),('3','酒店管理');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `cno` bigint NOT NULL AUTO_INCREMENT,
  `cname` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `sec` varchar(255) NOT NULL,
  `site` varchar(255) NOT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'资本论','Mon','1','基a-116'),(20,'舞蹈','Mon','2','基a-202'),(21,'说学逗唱','Mon','4','基c-203'),(22,'忽悠论','Tue','1','基d-202'),(23,'接化发','Wed','2','基a-208'),(24,'钞能力','Thu','3','基c-333'),(25,'刻薄学','Fri','2','基a-255'),(26,'吹拉弹唱','Thu','2','基c-208'),(27,'认识新冠','Fri','1','基a-230'),(28,'武德','Wed','3','基a-111'),(29,'厌金学','Fri','4','基a-250'),(30,'好自为之','Tue','2','基c-208');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `sno` varchar(255) NOT NULL,
  `sname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `s_cid` varchar(255) NOT NULL,
  `s_sex` varchar(255) NOT NULL,
  `s_tel` varchar(255) NOT NULL,
  `s_mail` varchar(255) NOT NULL,
  `s_birth` varchar(255) NOT NULL,
  PRIMARY KEY (`sno`),
  KEY `Student_class_cid_fk` (`s_cid`),
  CONSTRAINT `Student_class_cid_fk` FOREIGN KEY (`s_cid`) REFERENCES `class` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('201807010114','胖虎','123','3','男','444444','4@bucea.s.com','1964/06/15'),('201807010116','罗斯','123','1','男','13552121401','2@bucea.s.com','1988/10/04'),('201807010123','静香','123','3','女','222222','5@bucea.s.com','1964/05/02'),('201807010124','雪村','123','2','男','6532-7189','3@bucea.s.com','1969/04/01'),('201807010127','李易峰','123','1','男','333666','1@bucea.s.com','1987/05/04'),('s1','test','123','2','男','123333','6@bucea.s.com','2000/01/01');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teach`
--

DROP TABLE IF EXISTS `teach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teach` (
  `t_tno` varchar(255) NOT NULL,
  `t_cno` bigint NOT NULL,
  PRIMARY KEY (`t_tno`,`t_cno`),
  KEY `Teach_course_cno_fk` (`t_cno`),
  CONSTRAINT `teach_course_cno_fk` FOREIGN KEY (`t_cno`) REFERENCES `course` (`cno`),
  CONSTRAINT `Teach_teacher_tno_fk` FOREIGN KEY (`t_tno`) REFERENCES `teacher` (`tno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teach`
--

LOCK TABLES `teach` WRITE;
/*!40000 ALTER TABLE `teach` DISABLE KEYS */;
INSERT INTO `teach` VALUES ('20001',1),('20002',20),('20003',21),('20004',22),('20005',23),('20001',24),('20002',25),('20003',26),('20004',27),('20005',28),('20001',29),('20005',30);
/*!40000 ALTER TABLE `teach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `tno` varchar(255) NOT NULL,
  `tname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `tel` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `birth` varchar(255) NOT NULL,
  PRIMARY KEY (`tno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('20001','马云','123','男','9510211','1@bucea.t.com','1964/09/10'),('20002','金星','123','女','123123','2@bucea.t.com','1967/08/13'),('20003','郭德纲','123','男','234234','3@bucea.t.com','1973/01/18'),('20004','特朗普','123','男','456456','4@bucea.t.com','1946/06/14'),('20005','马保国','123','男','789789','5@bucea.t.com','1952/09/21'),('t1','test teacher','123','女','123123','6@bucea.t.com','1990/01/01');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-16 22:40:59
