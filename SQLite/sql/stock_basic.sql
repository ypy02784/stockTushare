/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:19:04
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for stock_basic
-- ----------------------------
DROP TABLE IF EXISTS "stock_basic";
CREATE TABLE "stock_basic" (
  "ts_code" TEXT(255),
  "symbol" TEXT(255),
  "name" TEXT(255),
  "area" TEXT(255),
  "industry" TEXT(255),
  "fullname" TEXT(255),
  "enname" TEXT(255),
  "market" TEXT(255),
  "exchange" TEXT(255),
  "curr_type" TEXT(255),
  "list_status" TEXT(255),
  "list_date" TEXT(255),
  "delist_date" TEXT(255),
  "is_hs" TEXT(255)
);

PRAGMA foreign_keys = true;
