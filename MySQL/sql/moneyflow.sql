/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 100136
 Source Host           : localhost:3306
 Source Schema         : stocktushare

 Target Server Type    : MySQL
 Target Server Version : 100136
 File Encoding         : 65001

 Date: 18/03/2019 21:30:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for moneyflow
-- ----------------------------
DROP TABLE IF EXISTS `moneyflow`;
CREATE TABLE `moneyflow`  (
  `ts_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TS代码',
  `trade_date` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '交易日期',
  `buy_sm_vol` int(20) NULL DEFAULT NULL COMMENT '小单买入量（手）',
  `buy_sm_amount` float(20, 0) NULL DEFAULT NULL COMMENT '小单买入金额（万元）',
  `sell_sm_vol` int(20) NULL DEFAULT NULL COMMENT '小单卖出量（手）',
  `sell_sm_amount` float(20, 0) NULL DEFAULT NULL COMMENT '小单卖出金额（万元）',
  `buy_md_vol` int(20) NULL DEFAULT NULL COMMENT '中单买入量（手）',
  `buy_md_amount` float(20, 0) NULL DEFAULT NULL COMMENT '中单买入金额（万元）',
  `sell_md_vol` int(20) NULL DEFAULT NULL COMMENT '中单卖出量（手）',
  `sell_md_amount` float(20, 0) NULL DEFAULT NULL COMMENT '中单卖出金额（万元）',
  `buy_lg_vol` int(20) NULL DEFAULT NULL COMMENT '大单买入量（手）',
  `buy_lg_amount` float(20, 0) NULL DEFAULT NULL COMMENT '大单买入金额（万元）',
  `sell_lg_vol` int(20) NULL DEFAULT NULL COMMENT '大单卖出量（手）',
  `sell_lg_amount` float(20, 0) NULL DEFAULT NULL COMMENT '大单卖出金额（万元）',
  `buy_elg_vol` int(20) NULL DEFAULT NULL COMMENT '特大单买入量（手）',
  `buy_elg_amount` float(20, 0) NOT NULL COMMENT '特大单买入金额（万元）',
  `sell_elg_vol` int(20) NULL DEFAULT NULL COMMENT '特大单卖出量（手）',
  `sell_elg_amount` float(20, 0) NULL DEFAULT NULL COMMENT '特大单卖出金额（万元）',
  `net_mf_vol` int(20) NULL DEFAULT NULL COMMENT '净流入量（手）',
  `net_mf_amount` float(20, 0) NULL DEFAULT NULL COMMENT '净流入额（万元）'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
