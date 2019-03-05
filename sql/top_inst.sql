/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 100136
 Source Host           : localhost:3306
 Source Schema         : stocktushare

 Target Server Type    : MySQL
 Target Server Version : 100136
 File Encoding         : 65001

 Date: 05/03/2019 09:30:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for top_inst
-- ----------------------------
DROP TABLE IF EXISTS `top_inst`;
CREATE TABLE `top_inst`  (
  `trade_date` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '交易日期',
  `ts_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TS代码',
  `exalter` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '营业部名称',
  `buy` float(255, 0) NULL DEFAULT NULL COMMENT '买入额（万）',
  `buy_rate` float(255, 0) NULL DEFAULT NULL COMMENT '买入占总成交比例',
  `sell` float(255, 0) NULL DEFAULT NULL COMMENT '卖出额（万',
  `sell_rate` float(255, 0) NULL DEFAULT NULL COMMENT '卖出占总成交比例',
  `net_buy` float(255, 0) NULL DEFAULT NULL COMMENT '净成交额（万）'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
