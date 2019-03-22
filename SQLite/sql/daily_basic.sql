/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:18:58
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for daily_basic
-- ----------------------------
CREATE TABLE  IF NOT EXISTS "daily_basic" (
  "ts_code" TEXT(255),
  "trade_date" TEXT(255),
  "close" REAL(255),
  "turnover_rate" REAL(255),
  "turnover_rate_f" REAL(255),
  "volume_ratio" REAL(255),
  "pe" REAL(255),
  "pe_ttm" REAL(255),
  "pb" REAL(255),
  "ps" REAL(255),
  "ps_ttm" REAL(255),
  "total_share" REAL(255),
  "float_share" TEXT(255),
  "free_share" TEXT(255),
  "total_mv" TEXT(255),
  "circ_mv" TEXT(255)
);

PRAGMA foreign_keys = true;
