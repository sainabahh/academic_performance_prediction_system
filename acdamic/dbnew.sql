/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - academic
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`academic` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `academic`;

/*Table structure for table `acd_app_allocate_table` */

DROP TABLE IF EXISTS `acd_app_allocate_table`;

CREATE TABLE `acd_app_allocate_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `staff_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_allocate_tab_staff_id_92bcf42f_fk_acd_app_s` (`staff_id`),
  KEY `acd_app_allocate_tab_subject_id_7d3f68df_fk_acd_app_s` (`subject_id`),
  CONSTRAINT `acd_app_allocate_tab_staff_id_92bcf42f_fk_acd_app_s` FOREIGN KEY (`staff_id`) REFERENCES `acd_app_staff_table` (`id`),
  CONSTRAINT `acd_app_allocate_tab_subject_id_7d3f68df_fk_acd_app_s` FOREIGN KEY (`subject_id`) REFERENCES `acd_app_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_allocate_table` */

insert  into `acd_app_allocate_table`(`id`,`staff_id`,`subject_id`) values 
(1,2,1);

/*Table structure for table `acd_app_complaint_table` */

DROP TABLE IF EXISTS `acd_app_complaint_table`;

CREATE TABLE `acd_app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` longtext NOT NULL,
  `reply` longtext NOT NULL,
  `date` date NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_complaint_ta_STAFF_id_05cd594e_fk_acd_app_s` (`STAFF_id`),
  KEY `acd_app_complaint_ta_student_id_2699b1af_fk_acd_app_s` (`student_id`),
  CONSTRAINT `acd_app_complaint_ta_STAFF_id_05cd594e_fk_acd_app_s` FOREIGN KEY (`STAFF_id`) REFERENCES `acd_app_staff_table` (`id`),
  CONSTRAINT `acd_app_complaint_ta_student_id_2699b1af_fk_acd_app_s` FOREIGN KEY (`student_id`) REFERENCES `acd_app_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_complaint_table` */

insert  into `acd_app_complaint_table`(`id`,`complaint`,`reply`,`date`,`STAFF_id`,`student_id`) values 
(1,'network issues','sry','2024-04-22',2,1);

/*Table structure for table `acd_app_course_table` */

DROP TABLE IF EXISTS `acd_app_course_table`;

CREATE TABLE `acd_app_course_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `coursename` varchar(1000) NOT NULL,
  `details` varchar(900) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_course_table` */

insert  into `acd_app_course_table`(`id`,`coursename`,`details`,`date`) values 
(1,'bsc cs','BSc Computer Science or Bachelor of Science in Computer Science course is an undergraduate degree programme that provides knowledge on various computer systems, software, and related technologies','2024-04-21');

/*Table structure for table `acd_app_doubt_table` */

DROP TABLE IF EXISTS `acd_app_doubt_table`;

CREATE TABLE `acd_app_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` longtext NOT NULL,
  `reply` longtext NOT NULL,
  `staff_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_doubt_table_staff_id_e05e44b2_fk_acd_app_staff_table_id` (`staff_id`),
  KEY `acd_app_doubt_table_student_id_b775e6bd_fk_acd_app_s` (`student_id`),
  KEY `acd_app_doubt_table_subject_id_8e3639ff_fk_acd_app_s` (`subject_id`),
  CONSTRAINT `acd_app_doubt_table_staff_id_e05e44b2_fk_acd_app_staff_table_id` FOREIGN KEY (`staff_id`) REFERENCES `acd_app_staff_table` (`id`),
  CONSTRAINT `acd_app_doubt_table_student_id_b775e6bd_fk_acd_app_s` FOREIGN KEY (`student_id`) REFERENCES `acd_app_student_table` (`id`),
  CONSTRAINT `acd_app_doubt_table_subject_id_8e3639ff_fk_acd_app_s` FOREIGN KEY (`subject_id`) REFERENCES `acd_app_subject_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_doubt_table` */

/*Table structure for table `acd_app_feedback_table` */

DROP TABLE IF EXISTS `acd_app_feedback_table`;

CREATE TABLE `acd_app_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `date` date NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_feedback_tab_student_id_930e0433_fk_acd_app_s` (`student_id`),
  KEY `acd_app_feedback_tab_subject_id_82668092_fk_acd_app_s` (`subject_id`),
  CONSTRAINT `acd_app_feedback_tab_student_id_930e0433_fk_acd_app_s` FOREIGN KEY (`student_id`) REFERENCES `acd_app_student_table` (`id`),
  CONSTRAINT `acd_app_feedback_tab_subject_id_82668092_fk_acd_app_s` FOREIGN KEY (`subject_id`) REFERENCES `acd_app_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_feedback_table` */

insert  into `acd_app_feedback_table`(`id`,`feedback`,`date`,`student_id`,`subject_id`) values 
(1,'good','2024-04-22',1,1);

/*Table structure for table `acd_app_login_table` */

DROP TABLE IF EXISTS `acd_app_login_table`;

CREATE TABLE `acd_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `type` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_login_table` */

insert  into `acd_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(3,'kiran','kiran@123','staff'),
(5,'anu','anu@1234','student');

/*Table structure for table `acd_app_staff_noti_table` */

DROP TABLE IF EXISTS `acd_app_staff_noti_table`;

CREATE TABLE `acd_app_staff_noti_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_time` datetime(6) NOT NULL,
  `content` varchar(100) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `SUBID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_staff_noti_t_STAFF_id_4ebbbefc_fk_acd_app_s` (`STAFF_id`),
  KEY `acd_app_staff_noti_t_SUBID_id_cc432b10_fk_acd_app_a` (`SUBID_id`),
  CONSTRAINT `acd_app_staff_noti_t_STAFF_id_4ebbbefc_fk_acd_app_s` FOREIGN KEY (`STAFF_id`) REFERENCES `acd_app_staff_table` (`id`),
  CONSTRAINT `acd_app_staff_noti_t_SUBID_id_cc432b10_fk_acd_app_a` FOREIGN KEY (`SUBID_id`) REFERENCES `acd_app_allocate_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_staff_noti_table` */

insert  into `acd_app_staff_noti_table`(`id`,`date_time`,`content`,`STAFF_id`,`SUBID_id`) values 
(1,'2024-04-22 16:54:15.735789','ffffff',2,1);

/*Table structure for table `acd_app_staff_table` */

DROP TABLE IF EXISTS `acd_app_staff_table`;

CREATE TABLE `acd_app_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(1000) NOT NULL,
  `lname` varchar(1000) NOT NULL,
  `gender` varchar(1000) NOT NULL,
  `place` varchar(1000) NOT NULL,
  `post` varchar(1000) NOT NULL,
  `pin` int NOT NULL,
  `email` varchar(1000) NOT NULL,
  `phone` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  `login_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_staff_table_login_id_06340b70_fk_acd_app_login_table_id` (`login_id`),
  CONSTRAINT `acd_app_staff_table_login_id_06340b70_fk_acd_app_login_table_id` FOREIGN KEY (`login_id`) REFERENCES `acd_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_staff_table` */

insert  into `acd_app_staff_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`email`,`phone`,`image`,`login_id`) values 
(2,'kiran','kumar','Male','kozikode','mukkam',767878,'kiran@gmail.com',7878787878,'download_px2CzxK.jpeg',3);

/*Table structure for table `acd_app_student_table` */

DROP TABLE IF EXISTS `acd_app_student_table`;

CREATE TABLE `acd_app_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(1000) NOT NULL,
  `lname` varchar(1000) NOT NULL,
  `gender` varchar(1000) NOT NULL,
  `place` varchar(1000) NOT NULL,
  `post` varchar(1000) NOT NULL,
  `pin` int NOT NULL,
  `email` varchar(1000) NOT NULL,
  `contact` bigint NOT NULL,
  `dob` date NOT NULL,
  `image` varchar(100) NOT NULL,
  `course_id` bigint NOT NULL,
  `login_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_student_tabl_course_id_5aaaa18e_fk_acd_app_c` (`course_id`),
  KEY `acd_app_student_tabl_login_id_9b31ce1b_fk_acd_app_l` (`login_id`),
  CONSTRAINT `acd_app_student_tabl_course_id_5aaaa18e_fk_acd_app_c` FOREIGN KEY (`course_id`) REFERENCES `acd_app_course_table` (`id`),
  CONSTRAINT `acd_app_student_tabl_login_id_9b31ce1b_fk_acd_app_l` FOREIGN KEY (`login_id`) REFERENCES `acd_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_student_table` */

insert  into `acd_app_student_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`email`,`contact`,`dob`,`image`,`course_id`,`login_id`) values 
(1,'anu','mol','on','kodayam','kollamchena',787878,'anumol@gmail.com',9878987898,'2005-07-06','Dora-Copy_qRWKXv1.jpg',1,5);

/*Table structure for table `acd_app_studentperformance_table` */

DROP TABLE IF EXISTS `acd_app_studentperformance_table`;

CREATE TABLE `acd_app_studentperformance_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `grade` varchar(1000) NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_studentperfo_student_id_ddf710b4_fk_acd_app_s` (`student_id`),
  KEY `acd_app_studentperfo_subject_id_0476e343_fk_acd_app_s` (`subject_id`),
  CONSTRAINT `acd_app_studentperfo_student_id_ddf710b4_fk_acd_app_s` FOREIGN KEY (`student_id`) REFERENCES `acd_app_student_table` (`id`),
  CONSTRAINT `acd_app_studentperfo_subject_id_0476e343_fk_acd_app_s` FOREIGN KEY (`subject_id`) REFERENCES `acd_app_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_studentperformance_table` */

insert  into `acd_app_studentperformance_table`(`id`,`grade`,`student_id`,`subject_id`) values 
(2,'B+',1,1);

/*Table structure for table `acd_app_studymaterials_tables` */

DROP TABLE IF EXISTS `acd_app_studymaterials_tables`;

CREATE TABLE `acd_app_studymaterials_tables` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `material` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `topic` varchar(900) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_studymateria_STAFF_id_9fb069d9_fk_acd_app_s` (`STAFF_id`),
  KEY `acd_app_studymateria_subject_id_626354be_fk_acd_app_s` (`subject_id`),
  CONSTRAINT `acd_app_studymateria_STAFF_id_9fb069d9_fk_acd_app_s` FOREIGN KEY (`STAFF_id`) REFERENCES `acd_app_staff_table` (`id`),
  CONSTRAINT `acd_app_studymateria_subject_id_626354be_fk_acd_app_s` FOREIGN KEY (`subject_id`) REFERENCES `acd_app_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_studymaterials_tables` */

insert  into `acd_app_studymaterials_tables`(`id`,`material`,`date`,`topic`,`STAFF_id`,`subject_id`) values 
(1,'requirements_OmXQ559.docx','2024-04-21','chapter1',2,1);

/*Table structure for table `acd_app_subject_table` */

DROP TABLE IF EXISTS `acd_app_subject_table`;

CREATE TABLE `acd_app_subject_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(1000) NOT NULL,
  `details` varchar(900) NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_subject_tabl_course_id_ea0bc131_fk_acd_app_c` (`course_id`),
  CONSTRAINT `acd_app_subject_tabl_course_id_ea0bc131_fk_acd_app_c` FOREIGN KEY (`course_id`) REFERENCES `acd_app_course_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_subject_table` */

insert  into `acd_app_subject_table`(`id`,`subject`,`details`,`course_id`) values 
(1,'MATHS','Mathematics is the science and study of quality, structure, space, and change. Mathematicians seek out patterns, formulate new conjectures, and establish truth by rigorous deduction from appropriately chosen axioms and definitions.',1);

/*Table structure for table `acd_app_work_result` */

DROP TABLE IF EXISTS `acd_app_work_result`;

CREATE TABLE `acd_app_work_result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_time` datetime(6) NOT NULL,
  `report` varchar(100) NOT NULL,
  `remark` varchar(30) NOT NULL,
  `mark` double NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  `WORK_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acd_app_work_result_STUDENT_id_9b86f7d1_fk_acd_app_s` (`STUDENT_id`),
  KEY `acd_app_work_result_WORK_id_0a0341c3_fk_acd_app_s` (`WORK_id`),
  CONSTRAINT `acd_app_work_result_STUDENT_id_9b86f7d1_fk_acd_app_s` FOREIGN KEY (`STUDENT_id`) REFERENCES `acd_app_student_table` (`id`),
  CONSTRAINT `acd_app_work_result_WORK_id_0a0341c3_fk_acd_app_s` FOREIGN KEY (`WORK_id`) REFERENCES `acd_app_staff_noti_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `acd_app_work_result` */

insert  into `acd_app_work_result`(`id`,`date_time`,`report`,`remark`,`mark`,`STUDENT_id`,`WORK_id`) values 
(3,'2024-04-23 10:38:00.032357','cart.png','not bad',3.7,1,1);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add course_table',7,'add_course_table'),
(26,'Can change course_table',7,'change_course_table'),
(27,'Can delete course_table',7,'delete_course_table'),
(28,'Can view course_table',7,'view_course_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add staff_table',9,'add_staff_table'),
(34,'Can change staff_table',9,'change_staff_table'),
(35,'Can delete staff_table',9,'delete_staff_table'),
(36,'Can view staff_table',9,'view_staff_table'),
(37,'Can add student_table',10,'add_student_table'),
(38,'Can change student_table',10,'change_student_table'),
(39,'Can delete student_table',10,'delete_student_table'),
(40,'Can view student_table',10,'view_student_table'),
(41,'Can add subject_table',11,'add_subject_table'),
(42,'Can change subject_table',11,'change_subject_table'),
(43,'Can delete subject_table',11,'delete_subject_table'),
(44,'Can view subject_table',11,'view_subject_table'),
(45,'Can add studymaterials_tables',12,'add_studymaterials_tables'),
(46,'Can change studymaterials_tables',12,'change_studymaterials_tables'),
(47,'Can delete studymaterials_tables',12,'delete_studymaterials_tables'),
(48,'Can view studymaterials_tables',12,'view_studymaterials_tables'),
(49,'Can add studentperformance_table',13,'add_studentperformance_table'),
(50,'Can change studentperformance_table',13,'change_studentperformance_table'),
(51,'Can delete studentperformance_table',13,'delete_studentperformance_table'),
(52,'Can view studentperformance_table',13,'view_studentperformance_table'),
(53,'Can add feedback_table',14,'add_feedback_table'),
(54,'Can change feedback_table',14,'change_feedback_table'),
(55,'Can delete feedback_table',14,'delete_feedback_table'),
(56,'Can view feedback_table',14,'view_feedback_table'),
(57,'Can add doubt_table',15,'add_doubt_table'),
(58,'Can change doubt_table',15,'change_doubt_table'),
(59,'Can delete doubt_table',15,'delete_doubt_table'),
(60,'Can view doubt_table',15,'view_doubt_table'),
(61,'Can add complaint_table',16,'add_complaint_table'),
(62,'Can change complaint_table',16,'change_complaint_table'),
(63,'Can delete complaint_table',16,'delete_complaint_table'),
(64,'Can view complaint_table',16,'view_complaint_table'),
(65,'Can add allocate_table',17,'add_allocate_table'),
(66,'Can change allocate_table',17,'change_allocate_table'),
(67,'Can delete allocate_table',17,'delete_allocate_table'),
(68,'Can view allocate_table',17,'view_allocate_table'),
(69,'Can add staff_noti_table',18,'add_staff_noti_table'),
(70,'Can change staff_noti_table',18,'change_staff_noti_table'),
(71,'Can delete staff_noti_table',18,'delete_staff_noti_table'),
(72,'Can view staff_noti_table',18,'view_staff_noti_table'),
(73,'Can add work_result',19,'add_work_result'),
(74,'Can change work_result',19,'change_work_result'),
(75,'Can delete work_result',19,'delete_work_result'),
(76,'Can view work_result',19,'view_work_result');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$Q6PldwLDU0V0tCSh4oi1pm$qBhTVijuNm6/31TZO3mZtfWqZKwz+QDJLbggphKC7I4=','2024-04-23 05:08:20.988884',1,'admin','','','admin@gmail.com',1,1,'2024-04-21 07:12:57.195310');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(17,'acd_app','allocate_table'),
(16,'acd_app','complaint_table'),
(7,'acd_app','course_table'),
(15,'acd_app','doubt_table'),
(14,'acd_app','feedback_table'),
(8,'acd_app','login_table'),
(18,'acd_app','staff_noti_table'),
(9,'acd_app','staff_table'),
(10,'acd_app','student_table'),
(13,'acd_app','studentperformance_table'),
(12,'acd_app','studymaterials_tables'),
(11,'acd_app','subject_table'),
(19,'acd_app','work_result'),
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'acd_app','0001_initial','2024-04-21 07:07:49.442491'),
(2,'contenttypes','0001_initial','2024-04-21 07:07:49.557765'),
(3,'auth','0001_initial','2024-04-21 07:07:50.665510'),
(4,'admin','0001_initial','2024-04-21 07:07:50.924136'),
(5,'admin','0002_logentry_remove_auto_add','2024-04-21 07:07:50.937463'),
(6,'admin','0003_logentry_add_action_flag_choices','2024-04-21 07:07:50.951178'),
(7,'contenttypes','0002_remove_content_type_name','2024-04-21 07:07:51.422065'),
(8,'auth','0002_alter_permission_name_max_length','2024-04-21 07:07:51.562486'),
(9,'auth','0003_alter_user_email_max_length','2024-04-21 07:07:51.593942'),
(10,'auth','0004_alter_user_username_opts','2024-04-21 07:07:51.605909'),
(11,'auth','0005_alter_user_last_login_null','2024-04-21 07:07:51.662642'),
(12,'auth','0006_require_contenttypes_0002','2024-04-21 07:07:51.666664'),
(13,'auth','0007_alter_validators_add_error_messages','2024-04-21 07:07:51.677399'),
(14,'auth','0008_alter_user_username_max_length','2024-04-21 07:07:51.785854'),
(15,'auth','0009_alter_user_last_name_max_length','2024-04-21 07:07:52.001688'),
(16,'auth','0010_alter_group_name_max_length','2024-04-21 07:07:52.094541'),
(17,'auth','0011_update_proxy_permissions','2024-04-21 07:07:52.112656'),
(18,'auth','0012_alter_user_first_name_max_length','2024-04-21 07:07:52.197702'),
(19,'sessions','0001_initial','2024-04-21 07:07:52.284433'),
(20,'acd_app','0002_alter_course_table_details','2024-04-21 09:37:29.151053'),
(21,'acd_app','0003_alter_subject_table_details','2024-04-21 09:40:06.046035'),
(22,'acd_app','0004_auto_20240421_1539','2024-04-21 10:09:21.643816'),
(23,'acd_app','0005_staff_noti_table_work_result','2024-04-22 11:09:32.635037');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('9zboelmo275tw3198g1z3w2wpl860v7e','.eJxVjjsOwyAQBe9CHSFY802ZPmdAywKxE8uWwK6i3D0hcuN23mj03myeErsOFxZw38awt1xDJ0yyE4tIr7z0IT1xeayc1mWrU-Rd4cfa-H1Neb4d7ikwYht7VsYBrdEAgMIqZaFoLV2yJmEhLT2SssJ5F72ADJoymRKp2KFgBu9_0fp__PkCBsk73A:1rz8OK:lD0mrofk2k5HoG3Oc7UsivrkwugZQ5S82aCTe8QDDL0','2024-05-07 05:08:28.084064');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
