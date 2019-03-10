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

 Date: 05/03/2019 09:30:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for top_list
-- ----------------------------
DROP TABLE IF EXISTS `top_list`;
CREATE TABLE `top_list`  (
  `trade_date` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '交易日期',
  `ts_code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'TS代码',
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `close` float(255, 0) NULL DEFAULT NULL COMMENT '收盘价',
  `pct_change` float(255, 0) NULL DEFAULT NULL COMMENT '涨跌幅',
  `turnover_rate` float(255, 0) NULL DEFAULT NULL COMMENT '换手率',
  `amount` float(255, 0) NULL DEFAULT NULL COMMENT '总成交额',
  `l_sell` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜卖出额',
  `l_buy` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜买入额',
  `l_amount` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜成交额',
  `net_amount` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜净买入额',
  `net_rate` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜净买额占比',
  `amount_rate` float(255, 0) NULL DEFAULT NULL COMMENT '龙虎榜成交额占比',
  `float_values` float(255, 0) NULL DEFAULT NULL COMMENT '当日流通市值',
  `reason` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '上榜理由'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
