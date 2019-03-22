/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 09/03/2019 22:19:09
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for stock_company
-- ----------------------------
CREATE TABLE  IF NOT EXISTS "stock_company" (
  "ts_code" TEXT(255),
  "exchange" TEXT(255),
  "chairman" TEXT(255),
  "manager" TEXT(255),
  "secretary" TEXT(255),
  "reg_capital" TEXT(255),
  "setup_date" TEXT(255),
  "province" TEXT(255),
  "city" TEXT(255),
  "introduction" TEXT(255),
  "website" TEXT(255),
  "email" TEXT(255),
  "office" TEXT(255),
  "employees" TEXT(255),
  "main_business" TEXT(255),
  "business_scope" TEXT(255)
);

PRAGMA foreign_keys = true;
