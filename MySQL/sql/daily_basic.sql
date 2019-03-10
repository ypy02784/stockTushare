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

 Date: 05/03/2019 09:30:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for daily_basic
-- ----------------------------
DROP TABLE IF EXISTS `daily_basic`;
CREATE TABLE `daily_basic`  (
  `ts_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TS股票代码',
  `trade_date` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '交易日期',
  `close` float NULL DEFAULT NULL COMMENT '当日收盘价',
  `turnover_rate` float NULL DEFAULT NULL COMMENT '换手率（%）',
  `turnover_rate_f` float NULL DEFAULT NULL COMMENT '换手率（自由流通股）',
  `volume_ratio` float NULL DEFAULT NULL COMMENT '量比',
  `pe` float NULL DEFAULT NULL COMMENT '	市盈率（总市值/净利润）',
  `pe_ttm` float NULL DEFAULT NULL COMMENT '	市盈率（TTM）',
  `pb` float NULL DEFAULT NULL COMMENT '市净率（总市值/净资产）',
  `ps` float NULL DEFAULT NULL COMMENT '	市销率',
  `ps_ttm` float NULL DEFAULT NULL COMMENT '市销率（TTM）',
  `total_share` float NULL DEFAULT NULL COMMENT '总股本 （万）',
  `float_share` float NULL DEFAULT NULL COMMENT '流通股本 （万）',
  `free_share` float NULL DEFAULT NULL COMMENT '自由流通股本 （万）',
  `total_mv` float NULL DEFAULT NULL COMMENT '总市值 （万元）',
  `circ_mv` float NULL DEFAULT NULL COMMENT '	流通市值（万元）'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
