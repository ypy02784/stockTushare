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

 Date: 05/03/2019 09:30:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for table_info
-- ----------------------------
DROP TABLE IF EXISTS `table_info`;
CREATE TABLE `table_info`  (
  `tablename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '数据表名称',
  `tableremark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '数据表备注',
  `column` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '列名',
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '列类型',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '列备注'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of table_info
-- ----------------------------
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'ts_code', 'str', 'TS代码');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'trade_date', 'str', '交易日历');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'price', 'float', '成交价');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'vol', 'float', '成交量（万股）');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'amount', 'float', '成交金额');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'buyer', 'str', '买方营业部');
INSERT INTO `table_info` VALUES ('block_trade', '大宗交易', 'seller', 'str', '卖房营业部');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'rade_date', 'str', '交易日期');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'ts_code', 'str', 'TS代码');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'exalter', 'str', '营业部名称');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'buy', 'float', '买入额（万）');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'buy_rate', 'float', '买入占总成交比例');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'sell', 'float', '卖出额（万）');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'sell_rate', 'float', '卖出占总成交比例');
INSERT INTO `table_info` VALUES ('top_inst', '龙虎榜机构明细', 'net_buy', 'float', '净成交额（万）');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'trade_date', 'str', '交易日期');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'ts_code', 'str', 'TS代码');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'name', 'str', '名称');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'close', 'float', '收盘价');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'pct_change', 'float', '涨跌幅');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'turnover_rate', 'float', '换手率');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'amount', 'float', '总成交额');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'l_sell', 'float', '龙虎榜卖出额');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'l_buy', 'float', '龙虎榜买入额');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'l_amount', 'float', '龙虎榜成交额');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'net_amount', 'float', '龙虎榜净买入额');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'net_rate', 'float', '龙虎榜净买额占比');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'amount_rate', 'float', '龙虎榜成交额占比');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'float_values', 'float', '当日流通市值');
INSERT INTO `table_info` VALUES ('top_list', '龙虎榜每日明细', 'reason', 'str', '上榜理由');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'ts_code', 'str', 'TS股票代码');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'trade_date', 'str', '交易日期');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'close', 'float', '当日收盘价');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'turnover_rate', 'float', '换手率（%）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'turnover_rate_f', 'float', '换手率（自由流通股）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'volume_ratio', 'float', '量比');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'pe', 'float', '市盈率（总市值/净利润）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'pe_ttm', 'float', '市盈率（TTM）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'pb', 'float', '市净率（总市值/净资产）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'ps', 'float', '市销率');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'ps_ttm', 'float', '市销率（TTM）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'total_share', 'float', '总股本 （万）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'float_share', 'float', '流通股本 （万）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'free_share', 'float', '自由流通股本 （万）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'total_mv', 'float', '总市值 （万元）');
INSERT INTO `table_info` VALUES ('daily_basic', '每日指标', 'circ_mv', 'float', '流通市值（万元）');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'ts_code', 'str', '股票代码');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'trade_date', 'str', '交易日期');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'open', 'float', '开盘价');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'high', 'float', '最高价');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'low', 'float', '最低价');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'close', 'float', '收盘价');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'pre_close', 'float', '昨收价');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'change', 'float', '涨跌额');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'pct_chg', 'float', '涨跌幅 （未复权，如果是复权请用 通用行情接口 ）');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'vol', 'float', '成交量 （手）');
INSERT INTO `table_info` VALUES ('daily', '日线行情', 'amount', 'float', '成交额 （千元）');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'ts_code', 'str', 'TS代码');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'symbol', 'str', '股票代码');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'name', 'str', '股票名称');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'area', 'str', '所在地域');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'industry', 'str', '所属行业');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'fullname', 'str', '股票全称');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'enname', 'str', '英文全称');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'market', 'str', '市场类型 （主板/中小板/创业板）');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'exchange', 'str', '交易所代码');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'curr_type', 'str', '交易货币');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'list_status', 'str', '上市状态： L上市 D退市 P暂停上市');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'list_date', 'str', '上市日期');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'delist_date', 'str', '退市日期');
INSERT INTO `table_info` VALUES ('stock_basic', '股票列表', 'is_hs', 'str', '是否沪深港通标的，N否 H沪股通 S深股通');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'ts_code', 'str', '股票代码');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'exchange', 'str', '交易所代码 ，SSE上交所 SZSE深交所');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'chairman', 'str', '法人代表');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'manager', 'str', '总经理');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'secretary', 'str', '董秘');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'reg_capital', 'float', '注册资本');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'setup_date', 'str', '注册日期');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'province', 'str', '所在省份');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'city', 'str', '所在城市');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'introduction', 'str', '公司介绍');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'website', 'str', '公司主页');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'email', 'str', '电子邮件');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'office', 'str', '办公室');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'employees', 'int', '员工人数');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'main_business', 'str', '主要业务及产品');
INSERT INTO `table_info` VALUES ('stock_company', '上市公司基本信息', 'business_scope', 'str', '经营范围');
INSERT INTO `table_info` VALUES ('table_info', '数据表信息', 'tablename', 'str', '数据表明');
INSERT INTO `table_info` VALUES ('table_info', '数据表信息', 'tableremark', 'str', '数据表备注');
INSERT INTO `table_info` VALUES ('table_info	', '数据表信息', 'column', 'str', '列名');
INSERT INTO `table_info` VALUES ('table_info	', '数据表信息', 'type', 'str', '列类别');
INSERT INTO `table_info` VALUES ('table_info	', '数据表信息', 'remark', 'str', '列备注');

SET FOREIGN_KEY_CHECKS = 1;
