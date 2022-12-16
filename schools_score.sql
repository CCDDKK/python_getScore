/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : college_score

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 08/12/2022 21:56:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for schools_score
-- ----------------------------
DROP TABLE IF EXISTS `schools_score`;
CREATE TABLE `schools_score`  (
  `年份` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `录取批次` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `招生类型` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `最低分/最低位次` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `省控线` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `专业组` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `选科要求` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `学校` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `地区` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `选测等级` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL
);

