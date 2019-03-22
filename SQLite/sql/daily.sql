/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:18:52
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for daily
-- ----------------------------
CREATE TABLE  IF NOT EXISTS "daily" (
  "ts_code" TEXT(255),
  "trade_date" TEXT(255),
  "open" REAL(255),
  "high" REAL(255),
  "low" REAL(255),
  "close" REAL(255),
  "pre_close" REAL(255),
  "change" REAL(255),
  "pct_chg" REAL(255),
  "vol" REAL(255),
  "amount" REAL(255)
);

PRAGMA foreign_keys = true;
