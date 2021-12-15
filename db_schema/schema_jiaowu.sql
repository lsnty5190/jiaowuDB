SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for classroom
-- ----------------------------
DROP TABLE IF EXISTS `classroom`;
CREATE TABLE `classroom` (
  `classroom_id` int NOT NULL,
  `address` varchar(40) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  PRIMARY KEY (`classroom_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `course_id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `dept_id` varchar(8) DEFAULT NULL,
  `course_english_name` varchar(150) DEFAULT NULL,
  `course_information_link` varchar(200) DEFAULT NULL,
  `credits` decimal(3,1) NOT NULL,
  PRIMARY KEY (`course_id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL,
  CONSTRAINT `course_chk_1` CHECK ((`credits` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `dept_id` varchar(8) NOT NULL,
  `dept_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for section
-- ----------------------------
DROP TABLE IF EXISTS `section`;
CREATE TABLE `section` (
  `course_id` varchar(10) NOT NULL,
  `sec_id` int NOT NULL,
  `year_semester` varchar(20) NOT NULL,
  `classroom_id` int DEFAULT NULL,
  `time_slot_id` int DEFAULT NULL,
  `enrollment` int DEFAULT NULL,
  PRIMARY KEY (`course_id`,`sec_id`,`year_semester`),
  UNIQUE KEY `section_uni` (`time_slot_id`,`classroom_id`, `year_semester`),
  KEY `classroom_id` (`classroom_id`),
  CONSTRAINT `section_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`) ON DELETE CASCADE,
  CONSTRAINT `section_ibfk_2` FOREIGN KEY (`classroom_id`) REFERENCES `classroom` (`classroom_id`) ON DELETE SET NULL,
  CONSTRAINT `section_ibfk_3` FOREIGN KEY (`time_slot_id`) REFERENCES `time_slot` (`time_slot_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `student_id` varchar(8) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `dept_id` varchar(8) DEFAULT NULL,
  `tot_credits` decimal(10,1) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for takes
-- ----------------------------
DROP TABLE IF EXISTS `takes`;
CREATE TABLE `takes` (
  `student_id` varchar(8) NOT NULL,
  `course_id` varchar(12) NOT NULL,
  `sec_id` int NOT NULL,
  `year_semester` varchar(20) NOT NULL,
  `grade` decimal(10,1) DEFAULT NULL,
  PRIMARY KEY (`student_id`,`course_id`,`sec_id`,`year_semester`),
  KEY `course_id` (`course_id`,`sec_id`,`year_semester`),
  CONSTRAINT `takes_ibfk_1` FOREIGN KEY (`course_id`, `sec_id`, `year_semester`) REFERENCES `section` (`course_id`, `sec_id`, `year_semester`) ON DELETE CASCADE,
  CONSTRAINT `takes_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `teacher_id` varchar(8) NOT NULL,
  `teacher_name` varchar(20) NOT NULL,
  `teacher_gender` tinyint DEFAULT NULL,
  `teacher_title` varchar(30) DEFAULT NULL,
  `teacher_nation` varchar(30) DEFAULT NULL,
  `teacher_phone` varchar(20) DEFAULT NULL,
  `teacher_email` varchar(45) DEFAULT NULL,
  `dept_id` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for teaches
-- ----------------------------
DROP TABLE IF EXISTS `teaches`;
CREATE TABLE `teaches` (
  `teacher_id` varchar(8) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `sec_id` int NOT NULL,
  `year_semester` varchar(20) NOT NULL,
  PRIMARY KEY (`teacher_id`,`course_id`,`sec_id`,`year_semester`),
  KEY `course_id` (`course_id`,`sec_id`,`year_semester`),
  CONSTRAINT `teaches_ibfk_1` FOREIGN KEY (`course_id`, `sec_id`, `year_semester`) REFERENCES `section` (`course_id`, `sec_id`, `year_semester`) ON DELETE CASCADE,
  CONSTRAINT `teaches_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for time_slot
-- ----------------------------
DROP TABLE IF EXISTS `time_slot`;
CREATE TABLE `time_slot` (
  `time_slot_id` int NOT NULL,
  `day` varchar(1) NOT NULL,
  `start_time` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `end_time` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`time_slot_id`,`day`) USING BTREE,
  KEY `time_slot_id` (`time_slot_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
