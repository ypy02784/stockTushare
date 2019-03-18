/*
 Navicat Premium Data Transfer

 Source Server         : stockTushare
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 18/03/2019 21:19:01
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for moneyflow
-- ----------------------------
DROP TABLE IF EXISTS "moneyflow";
CREATE TABLE "moneyflow" (
  "ts_code" TEXT(10),
  "trade_date" TEXT(10),
  "buy_sm_vol" INTEGER(20),
  "buy_sm_amount" REAL(20),
  "sell_sm_vol" INTEGER(20),
  "sell_sm_amount" REAL(20),
  "buy_md_vol" INTEGER(20),
  "buy_md_amount" REAL(20),
  "sell_md_vol" INTEGER(20),
  "sell_md_amount" REAL(20),
  "buy_lg_vol" INTEGER(20),
  "buy_lg_amount" REAL(20),
  "sell_lg_vol" INTEGER(20),
  "sell_lg_amount" REAL(20),
  "buy_elg_vol" INTEGER(20),
  "buy_elg_amount" REAL(20),
  "sell_elg_vol" INTEGER(20),
  "sell_elg_amount" REAL(20),
  "net_mf_vol" INTEGER(20),
  "net_mf_amount" REAL(20)
);

PRAGMA foreign_keys = true;
