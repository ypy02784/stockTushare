/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:19:28
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for top_list
-- ----------------------------
CREATE TABLE  IF NOT EXISTS "top_list" (
  "trade_date" TEXT(255),
  "ts_code" TEXT(255),
  "name" TEXT(255),
  "close" REAL(255),
  "pct_change" REAL(255),
  "turnover_rate" REAL(255),
  "amount" REAL(255),
  "l_sell" REAL(255),
  "l_buy" REAL(255),
  "l_amount" REAL(255),
  "net_amount" REAL(255),
  "net_rate" REAL(255),
  "amount_rate" TEXT(255),
  "float_values" TEXT(255),
  "reason" TEXT(255)
);

PRAGMA foreign_keys = true;
