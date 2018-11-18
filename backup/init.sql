-- MySQL dump 10.13  Distrib 5.7.22, for osx10.13 (x86_64)
--
-- Host: localhost    Database: common
-- ------------------------------------------------------
-- Server version	5.7.22

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 客户',7,'add_client'),(26,'Can change 客户',7,'change_client'),(27,'Can delete 客户',7,'delete_client'),(28,'Can view 客户',7,'view_client'),(29,'Can add 仓库',8,'add_depot'),(30,'Can change 仓库',8,'change_depot'),(31,'Can delete 仓库',8,'delete_depot'),(32,'Can view 仓库',8,'view_depot'),(33,'Can add 商品',9,'add_goods'),(34,'Can change 商品',9,'change_goods'),(35,'Can delete 商品',9,'delete_goods'),(36,'Can view 商品',9,'view_goods'),(37,'Can add 商品记录',10,'add_goodsrecord'),(38,'Can change 商品记录',10,'change_goodsrecord'),(39,'Can delete 商品记录',10,'delete_goodsrecord'),(40,'Can view 商品记录',10,'view_goodsrecord'),(41,'Can add 订单',11,'add_order'),(42,'Can change 订单',11,'change_order'),(43,'Can delete 订单',11,'delete_order'),(44,'Can view 订单',11,'view_order'),(45,'Can add 订单商品',12,'add_ordergoods'),(46,'Can change 订单商品',12,'change_ordergoods'),(47,'Can delete 订单商品',12,'delete_ordergoods'),(48,'Can view 订单商品',12,'view_ordergoods'),(49,'Can add 个人信息',13,'add_profile'),(50,'Can change 个人信息',13,'change_profile'),(51,'Can delete 个人信息',13,'delete_profile'),(52,'Can view 个人信息',13,'view_profile'),(53,'Can add 供应商',14,'add_supplier'),(54,'Can change 供应商',14,'change_supplier'),(55,'Can delete 供应商',14,'delete_supplier'),(56,'Can view 供应商',14,'view_supplier'),(57,'Can add goods damaged',15,'add_goodsdamaged'),(58,'Can change goods damaged',15,'change_goodsdamaged'),(59,'Can delete goods damaged',15,'delete_goodsdamaged'),(60,'Can view goods damaged',15,'view_goodsdamaged');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$v5c212QWKfgh$x6HTUYJ4uqxoI+ac15BdqodSfz8+CqNiD0OSpcs2D/M=','2018-11-18 20:06:37.805153',1,'admin','','','',1,1,'2018-11-18 20:06:21.823098');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-18 20:07:13.213957','1','老板',1,'[{\"added\": {}}]',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'new7','client'),(8,'new7','depot'),(9,'new7','goods'),(15,'new7','goodsdamaged'),(10,'new7','goodsrecord'),(11,'new7','order'),(12,'new7','ordergoods'),(13,'new7','profile'),(14,'new7','supplier'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-18 20:05:58.002002'),(2,'auth','0001_initial','2018-11-18 20:05:58.242986'),(3,'admin','0001_initial','2018-11-18 20:05:58.287560'),(4,'admin','0002_logentry_remove_auto_add','2018-11-18 20:05:58.300565'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-18 20:05:58.313908'),(6,'contenttypes','0002_remove_content_type_name','2018-11-18 20:05:58.370784'),(7,'auth','0002_alter_permission_name_max_length','2018-11-18 20:05:58.391141'),(8,'auth','0003_alter_user_email_max_length','2018-11-18 20:05:58.417166'),(9,'auth','0004_alter_user_username_opts','2018-11-18 20:05:58.427653'),(10,'auth','0005_alter_user_last_login_null','2018-11-18 20:05:58.449466'),(11,'auth','0006_require_contenttypes_0002','2018-11-18 20:05:58.453167'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-18 20:05:58.461341'),(13,'auth','0008_alter_user_username_max_length','2018-11-18 20:05:58.486916'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-18 20:05:58.534276'),(15,'new7','0001_initial','2018-11-18 20:05:58.985255'),(16,'new7','0002_goodsrecord_spec','2018-11-18 20:05:59.011672'),(17,'new7','0003_auto_20181110_1838','2018-11-18 20:05:59.029647'),(18,'new7','0004_goodsdamaged','2018-11-18 20:05:59.101734'),(19,'new7','0005_auto_20181113_2102','2018-11-18 20:05:59.360836'),(20,'new7','0006_goods_warn_stock','2018-11-18 20:05:59.397293'),(21,'new7','0007_auto_20181117_1525','2018-11-18 20:05:59.413188'),(22,'new7','0008_auto_20181117_1529','2018-11-18 20:05:59.426522'),(23,'sessions','0001_initial','2018-11-18 20:05:59.454854');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('rgok5848l1rzk8gy5sz9blzjb9w3uc2m','NDdiNzlkYTA4NjRkNjJiNzFkYmNiMjhjM2Q3MjE5N2UzMWViZGRmNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MTY0MDVkMmM5NTU5YzkwN2RmOWQ1YWE0ZDUwMjZmMmE5NmEyMjdjIn0=','2018-12-02 20:06:37.807264');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_client`
--

DROP TABLE IF EXISTS `new7_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `tontact_phone` varchar(20) DEFAULT NULL,
  `contact_name` varchar(20) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_client`
--

LOCK TABLES `new7_client` WRITE;
/*!40000 ALTER TABLE `new7_client` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_depot`
--

DROP TABLE IF EXISTS `new7_depot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_depot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `stock` int(11) NOT NULL,
  `cubage` int(11) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_depot`
--

LOCK TABLES `new7_depot` WRITE;
/*!40000 ALTER TABLE `new7_depot` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_depot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_goods`
--

DROP TABLE IF EXISTS `new7_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `short_name` varchar(100) DEFAULT NULL,
  `code` varchar(100) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `in_price` decimal(10,2) NOT NULL,
  `sale_price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `last_operate_type` varchar(20) DEFAULT NULL,
  `last_operate_time` datetime(6) DEFAULT NULL,
  `last_price` decimal(10,2) NOT NULL,
  `unit` varchar(100) DEFAULT NULL,
  `spec` varchar(100) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `is_book` tinyint(1) NOT NULL,
  `stock_status` int(11) NOT NULL,
  `last_operator_id` int(11) DEFAULT NULL,
  `warn_stock` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`),
  KEY `new7_goods_last_operator_id_344ae9ad_fk_new7_profile_id` (`last_operator_id`),
  CONSTRAINT `new7_goods_last_operator_id_344ae9ad_fk_new7_profile_id` FOREIGN KEY (`last_operator_id`) REFERENCES `new7_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_goods`
--

LOCK TABLES `new7_goods` WRITE;
/*!40000 ALTER TABLE `new7_goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_goodsdamaged`
--

DROP TABLE IF EXISTS `new7_goodsdamaged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_goodsdamaged` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `price` double NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `report_time` datetime(6) DEFAULT NULL,
  `remarks` longtext NOT NULL,
  `operator_id` int(11) DEFAULT NULL,
  `damaged_depot_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `new7_goodsdamaged_damaged_depot_id_435a65ec_fk_new7_depot_id` (`damaged_depot_id`),
  KEY `new7_goodsdamaged_goods_id_5463223d_fk_new7_goods_id` (`goods_id`),
  KEY `new7_goodsdamaged_operator_id_28ff1520` (`operator_id`),
  CONSTRAINT `new7_goodsdamaged_damaged_depot_id_435a65ec_fk_new7_depot_id` FOREIGN KEY (`damaged_depot_id`) REFERENCES `new7_depot` (`id`),
  CONSTRAINT `new7_goodsdamaged_goods_id_5463223d_fk_new7_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `new7_goods` (`id`),
  CONSTRAINT `new7_goodsdamaged_operator_id_28ff1520_fk_new7_profile_id` FOREIGN KEY (`operator_id`) REFERENCES `new7_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_goodsdamaged`
--

LOCK TABLES `new7_goodsdamaged` WRITE;
/*!40000 ALTER TABLE `new7_goodsdamaged` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_goodsdamaged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_goodsrecord`
--

DROP TABLE IF EXISTS `new7_goodsrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_goodsrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `record_type` varchar(20) NOT NULL,
  `count` int(11) NOT NULL,
  `leave_count` int(11) NOT NULL,
  `price` double DEFAULT NULL,
  `unit` varchar(200) DEFAULT NULL,
  `operator_account` varchar(20) DEFAULT NULL,
  `record_time` datetime(6) DEFAULT NULL,
  `record_source` varchar(50) NOT NULL,
  `remarks` longtext NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `record_depot_id` int(11) DEFAULT NULL,
  `spec` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `new7_goodsrecord_order_id_b5260f5a_fk_new7_order_id` (`order_id`),
  KEY `new7_goodsrecord_record_depot_id_ae686476_fk_new7_depot_id` (`record_depot_id`),
  KEY `new7_goodsrecord_goods_id_de889d8e_fk_new7_goods_id` (`goods_id`),
  CONSTRAINT `new7_goodsrecord_goods_id_de889d8e_fk_new7_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `new7_goods` (`id`),
  CONSTRAINT `new7_goodsrecord_order_id_b5260f5a_fk_new7_order_id` FOREIGN KEY (`order_id`) REFERENCES `new7_order` (`id`),
  CONSTRAINT `new7_goodsrecord_record_depot_id_ae686476_fk_new7_depot_id` FOREIGN KEY (`record_depot_id`) REFERENCES `new7_depot` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_goodsrecord`
--

LOCK TABLES `new7_goodsrecord` WRITE;
/*!40000 ALTER TABLE `new7_goodsrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_goodsrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_order`
--

DROP TABLE IF EXISTS `new7_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `invoice` varchar(100) DEFAULT NULL,
  `order_unique` varchar(200) DEFAULT NULL,
  `order_type` varchar(20) NOT NULL,
  `tontact_phone` varchar(20) DEFAULT NULL,
  `operator` varchar(200) DEFAULT NULL,
  `delivery_date` datetime(6) DEFAULT NULL,
  `deliver_type` varchar(200) DEFAULT NULL,
  `deliver_money` varchar(200) DEFAULT NULL,
  `deliver_address` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `total_count` int(11) NOT NULL,
  `pay_type` varchar(200) DEFAULT NULL,
  `pay_from` varchar(200) DEFAULT NULL,
  `is_pay` varchar(10) DEFAULT NULL,
  `remark` varchar(500) DEFAULT NULL,
  `is_closed` tinyint(1) NOT NULL,
  `flag` varchar(20) DEFAULT NULL,
  `trade_no` varchar(20) DEFAULT NULL,
  `is_refond` tinyint(1) NOT NULL,
  `depot_id` int(11) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice` (`invoice`),
  UNIQUE KEY `order_unique` (`order_unique`),
  KEY `new7_order_depot_id_d0d8f726_fk_new7_depot_id` (`depot_id`),
  KEY `new7_order_supplier_id_c91b2c9d_fk_new7_supplier_id` (`supplier_id`),
  CONSTRAINT `new7_order_depot_id_d0d8f726_fk_new7_depot_id` FOREIGN KEY (`depot_id`) REFERENCES `new7_depot` (`id`),
  CONSTRAINT `new7_order_supplier_id_c91b2c9d_fk_new7_supplier_id` FOREIGN KEY (`supplier_id`) REFERENCES `new7_supplier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_order`
--

LOCK TABLES `new7_order` WRITE;
/*!40000 ALTER TABLE `new7_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_ordergoods`
--

DROP TABLE IF EXISTS `new7_ordergoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_ordergoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `unit` varchar(200) DEFAULT NULL,
  `goods_id` int(11) DEFAULT NULL,
  `operate_depot_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `new7_ordergoods_goods_id_bd7032ca_fk_new7_goods_id` (`goods_id`),
  KEY `new7_ordergoods_operate_depot_id_c671988e_fk_new7_depot_id` (`operate_depot_id`),
  KEY `new7_ordergoods_order_id_dd55322e_fk_new7_order_id` (`order_id`),
  CONSTRAINT `new7_ordergoods_goods_id_bd7032ca_fk_new7_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `new7_goods` (`id`),
  CONSTRAINT `new7_ordergoods_operate_depot_id_c671988e_fk_new7_depot_id` FOREIGN KEY (`operate_depot_id`) REFERENCES `new7_depot` (`id`),
  CONSTRAINT `new7_ordergoods_order_id_dd55322e_fk_new7_order_id` FOREIGN KEY (`order_id`) REFERENCES `new7_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_ordergoods`
--

LOCK TABLES `new7_ordergoods` WRITE;
/*!40000 ALTER TABLE `new7_ordergoods` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_ordergoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_profile`
--

DROP TABLE IF EXISTS `new7_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `role` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` int(11) NOT NULL,
  `birth` datetime(6) DEFAULT NULL,
  `code` varchar(200) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `phone_verified` tinyint(1) NOT NULL,
  `address` varchar(20) DEFAULT NULL,
  `salary` int(11) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `depot_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `code` (`code`),
  KEY `new7_profile_content_type_id_59adc7b8_fk_django_content_type_id` (`content_type_id`),
  KEY `new7_profile_depot_id_96a33748_fk_new7_depot_id` (`depot_id`),
  CONSTRAINT `new7_profile_content_type_id_59adc7b8_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `new7_profile_depot_id_96a33748_fk_new7_depot_id` FOREIGN KEY (`depot_id`) REFERENCES `new7_depot` (`id`),
  CONSTRAINT `new7_profile_user_id_83b0aeb3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_profile`
--

LOCK TABLES `new7_profile` WRITE;
/*!40000 ALTER TABLE `new7_profile` DISABLE KEYS */;
INSERT INTO `new7_profile` VALUES (1,'2018-11-18 20:07:13.213068','2018-11-18 20:07:13.213101',0,1,'boss','老板',1,NULL,'1','10086',0,NULL,0,NULL,4,NULL,1);
/*!40000 ALTER TABLE `new7_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new7_supplier`
--

DROP TABLE IF EXISTS `new7_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new7_supplier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `license_code` varchar(20) DEFAULT NULL,
  `tontact_phone` varchar(20) DEFAULT NULL,
  `contact_name` varchar(20) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `operator` varchar(200) DEFAULT NULL,
  `operator_name` varchar(200) DEFAULT NULL,
  `desc` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new7_supplier`
--

LOCK TABLES `new7_supplier` WRITE;
/*!40000 ALTER TABLE `new7_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `new7_supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-18 20:07:28
