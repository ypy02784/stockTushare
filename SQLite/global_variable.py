import os

SYS_PATH = os.getcwd()
DB_TABLE_LIST = ['daily', 'daily_basic', 'stock_basic', 'stock_company', 'top_list', 'top_inst',
                 'block_trade', 'moneyflow', 'table_info']
DB_NAME = 'stockTushare'  # 系统使用的数据库名称
# DB_PATH = 'D:\stockTushare.db'  #数据库文件路径及名称
DB_PATH = 'stockTushare.db'  #相对地址数据库文件名称
DAILY_TABLE = 'daily'  # 股票每日交易信息表名称
DAILY_BASIC_TABLE = 'daily_basic'  # 股票每日交易信息指标表名称
STOCK_BASIC_TABLE = 'stock_basic'  # 股票基本信息表名称
COMPANY_TABLE = 'stock_company'  # 公司基本信息表名称
TOP_LIST_TABLE = 'top_list'  # 龙虎榜
TOP_INST_TABLE = 'top_inst'  # 龙虎榜机构交易
BLOCK_TRADE_TABLE = 'block_trade'  # 大宗交易
MONEYFLOW_TABLE = 'moneyflow'  # 个股资金流向
TABLE_INFO_TABLE = 'table_info'  # 所有数据表信息

TUSHARE_TOKEN = 'b5495988a3294331dda2b5c4a9bb7b9766f179863118c097e5296f60'  #tushare pro 网站的token

MODEL_HEADER_DICT = {}  #启动程序后应初始化该值，用以动态创建每个model的值
