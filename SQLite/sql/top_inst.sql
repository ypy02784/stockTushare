/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:19:24
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for top_inst
-- ----------------------------
CREATE TABLE  IF NOT EXISTS "top_inst" (
  "trade_date" TEXT(255),
  "ts_code" TEXT(255),
  "exalter" TEXT(255),
  "buy" REAL(255),
  "buy_rate" REAL(255),
  "sell" REAL(255),
  "sell_rate" REAL(255),
  "net_buy" REAL(255)
);

PRAGMA foreign_keys = true;
