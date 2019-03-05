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

 Date: 05/03/2019 09:30:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for daily
-- ----------------------------
DROP TABLE IF EXISTS `daily`;
CREATE TABLE `daily`  (
  `ts_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '股票代码',
  `trade_date` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '交易日期',
  `open` float NULL DEFAULT NULL COMMENT '开盘价',
  `high` float NULL DEFAULT NULL COMMENT '最高价',
  `low` float NULL DEFAULT NULL COMMENT '最低价',
  `close` float NULL DEFAULT NULL COMMENT '收盘价',
  `pre_close` float NULL DEFAULT NULL COMMENT '昨收价',
  `change` float NULL DEFAULT NULL COMMENT '涨跌额',
  `pct_chg` float NULL DEFAULT NULL COMMENT '	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）',
  `vol` float NULL DEFAULT NULL COMMENT '成交量 （手）',
  `amount` float NULL DEFAULT NULL COMMENT '成交额 （千元）'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
