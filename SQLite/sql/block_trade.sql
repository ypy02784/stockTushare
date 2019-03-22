/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:18:44
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for block_trade
-- ----------------------------
CREATE TABLE IF NOT EXISTS "block_trade" (
  "ts_code" TEXT(255),
  "trade_date" TEXT(255),
  "price" REAL(255),
  "vol" REAL(255),
  "amount" REAL(255),
  "buyer" TEXT(255),
  "seller" TEXT(255)
);

PRAGMA foreign_keys = true;
