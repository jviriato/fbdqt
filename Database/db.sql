-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Aluno`
--

DROP TABLE IF EXISTS `Aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Aluno` (
  `idAluno` int(11) NOT NULL AUTO_INCREMENT,
  `nomeAluno` varchar(45) NOT NULL,
  `matricula` int(11) NOT NULL,
  PRIMARY KEY (`idAluno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Aluno`
--

LOCK TABLES `Aluno` WRITE;
/*!40000 ALTER TABLE `Aluno` DISABLE KEYS */;
INSERT INTO `Aluno` VALUES (1,'Joao',2016001),(6,'Tobias',2016132),(7,'José',2013012);
/*!40000 ALTER TABLE `Aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Curso`
--

DROP TABLE IF EXISTS `Curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Curso` (
  `idCurso` int(11) NOT NULL AUTO_INCREMENT,
  `nomeCurso` varchar(45) NOT NULL,
  `siglaCurso` varchar(10) NOT NULL,
  PRIMARY KEY (`idCurso`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Curso`
--

LOCK TABLES `Curso` WRITE;
/*!40000 ALTER TABLE `Curso` DISABLE KEYS */;
INSERT INTO `Curso` VALUES (1,'Ciencia da Computacao','CiC '),(2,'Sistemas de Informacao','SI '),(3,'Eng. Comp.','ECOMP '),(4,'Eng. Ctrl. Aut.','ECA '),(5,'Medicina','MED '),(6,'Biologia','BIO '),(7,'Filosofia','FIL  '),(11,'Matematica','MAT ');
/*!40000 ALTER TABLE `Curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Curso_has_Disciplina`
--

DROP TABLE IF EXISTS `Curso_has_Disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Curso_has_Disciplina` (
  `Curso_idCurso` int(11) NOT NULL,
  `Disciplina_idDisciplina` int(11) NOT NULL,
  PRIMARY KEY (`Curso_idCurso`,`Disciplina_idDisciplina`),
  KEY `fk_Curso_has_Disciplina_Disciplina1_idx` (`Disciplina_idDisciplina`),
  KEY `fk_Curso_has_Disciplina_Curso1_idx` (`Curso_idCurso`),
  CONSTRAINT `fk_Curso_has_Disciplina_Curso1` FOREIGN KEY (`Curso_idCurso`) REFERENCES `Curso` (`idCurso`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Curso_has_Disciplina_Disciplina1` FOREIGN KEY (`Disciplina_idDisciplina`) REFERENCES `Disciplina` (`idDisciplina`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Curso_has_Disciplina`
--

LOCK TABLES `Curso_has_Disciplina` WRITE;
/*!40000 ALTER TABLE `Curso_has_Disciplina` DISABLE KEYS */;
INSERT INTO `Curso_has_Disciplina` VALUES (1,1),(2,1),(1,2),(2,2),(3,2),(1,5),(7,5),(1,6),(7,6),(7,7);
/*!40000 ALTER TABLE `Curso_has_Disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Disciplina`
--

DROP TABLE IF EXISTS `Disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Disciplina` (
  `idDisciplina` int(11) NOT NULL AUTO_INCREMENT,
  `nomeDisciplina` varchar(45) NOT NULL,
  PRIMARY KEY (`idDisciplina`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Disciplina`
--

LOCK TABLES `Disciplina` WRITE;
/*!40000 ALTER TABLE `Disciplina` DISABLE KEYS */;
INSERT INTO `Disciplina` VALUES (1,'Fundamento de Banco de Dados'),(2,'Algoritmos'),(4,'Lógica'),(5,'Filosofia'),(6,'Libras'),(7,'Libras II');
/*!40000 ALTER TABLE `Disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Frequencia`
--

DROP TABLE IF EXISTS `Frequencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Frequencia` (
  `idFrequencia` int(11) NOT NULL AUTO_INCREMENT,
  `Turma_idTurma` int(11) NOT NULL,
  `Aluno_idAluno` int(11) NOT NULL,
  `Data` date DEFAULT NULL,
  `Presenca` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`idFrequencia`,`Turma_idTurma`,`Aluno_idAluno`),
  KEY `fk_Turma_has_Aluno1_Aluno1_idx` (`Aluno_idAluno`),
  KEY `fk_Turma_has_Aluno1_Turma1_idx` (`Turma_idTurma`),
  CONSTRAINT `fk_Turma_has_Aluno1_Aluno1` FOREIGN KEY (`Aluno_idAluno`) REFERENCES `Aluno` (`idAluno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_has_Aluno1_Turma1` FOREIGN KEY (`Turma_idTurma`) REFERENCES `Turma` (`idTurma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Frequencia`
--

LOCK TABLES `Frequencia` WRITE;
/*!40000 ALTER TABLE `Frequencia` DISABLE KEYS */;
INSERT INTO `Frequencia` VALUES (1,1,1,'2016-01-01','P'),(2,1,1,'2016-01-02','F');
/*!40000 ALTER TABLE `Frequencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Professor`
--

DROP TABLE IF EXISTS `Professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Professor` (
  `idProfessor` int(11) NOT NULL AUTO_INCREMENT,
  `nomeProfessor` varchar(45) NOT NULL,
  `matricula` int(11) NOT NULL,
  PRIMARY KEY (`idProfessor`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Professor`
--

LOCK TABLES `Professor` WRITE;
/*!40000 ALTER TABLE `Professor` DISABLE KEYS */;
INSERT INTO `Professor` VALUES (1,'Luxemburgo',196021),(2,'Girafales',195022),(3,'Professorson',198201),(8,'Professor Doutor',321),(14,'Professional',212);
/*!40000 ALTER TABLE `Professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Turma`
--

DROP TABLE IF EXISTS `Turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Turma` (
  `idTurma` int(11) NOT NULL AUTO_INCREMENT,
  `nomeTurma` varchar(45) NOT NULL,
  `turno` varchar(45) NOT NULL,
  `Professor_idProfessor` int(11) NOT NULL,
  `Disciplina_idDisciplina` int(11) NOT NULL,
  `Data` date DEFAULT NULL,
  PRIMARY KEY (`idTurma`),
  KEY `fk_Turma_Professor_idx` (`Professor_idProfessor`),
  KEY `fk_Turma_Disciplina1_idx` (`Disciplina_idDisciplina`),
  CONSTRAINT `fk_Turma_Disciplina1` FOREIGN KEY (`Disciplina_idDisciplina`) REFERENCES `Disciplina` (`idDisciplina`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_Professor` FOREIGN KEY (`Professor_idProfessor`) REFERENCES `Professor` (`idProfessor`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Turma`
--

LOCK TABLES `Turma` WRITE;
/*!40000 ALTER TABLE `Turma` DISABLE KEYS */;
INSERT INTO `Turma` VALUES (1,'ELC001','Noturno',1,1,NULL),(2,'FBPA02','Diurno',2,2,NULL),(3,'SCCP03','Noturno',3,1,NULL);
/*!40000 ALTER TABLE `Turma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Turma_has_Aluno`
--

DROP TABLE IF EXISTS `Turma_has_Aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Turma_has_Aluno` (
  `Turma_idTurma` int(11) NOT NULL,
  `Aluno_idAluno` int(11) NOT NULL,
  PRIMARY KEY (`Turma_idTurma`,`Aluno_idAluno`),
  KEY `fk_Turma_has_Aluno_Aluno1_idx` (`Aluno_idAluno`),
  KEY `fk_Turma_has_Aluno_Turma1_idx` (`Turma_idTurma`),
  CONSTRAINT `fk_Turma_has_Aluno_Aluno1` FOREIGN KEY (`Aluno_idAluno`) REFERENCES `Aluno` (`idAluno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_has_Aluno_Turma1` FOREIGN KEY (`Turma_idTurma`) REFERENCES `Turma` (`idTurma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Turma_has_Aluno`
--

LOCK TABLES `Turma_has_Aluno` WRITE;
/*!40000 ALTER TABLE `Turma_has_Aluno` DISABLE KEYS */;
/*!40000 ALTER TABLE `Turma_has_Aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `curso_e_disc`
--

DROP TABLE IF EXISTS `curso_e_disc`;
/*!50001 DROP VIEW IF EXISTS `curso_e_disc`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `curso_e_disc` AS SELECT 
 1 AS `nomeCurso`,
 1 AS `nomeDisciplina`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `curso_e_disc`
--

/*!50001 DROP VIEW IF EXISTS `curso_e_disc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`viriato`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `curso_e_disc` AS select `c`.`nomeCurso` AS `nomeCurso`,`d`.`nomeDisciplina` AS `nomeDisciplina` from ((`Curso` `c` join `Curso_has_Disciplina` `cd`) join `Disciplina` `d`) where ((`c`.`idCurso` = `cd`.`Curso_idCurso`) and (`d`.`idDisciplina` = `cd`.`Disciplina_idDisciplina`)) order by `cd`.`Curso_idCurso` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-12  1:32:57
