import numpy as np
import pandas as pd
import os
from SQLite.connectSQLite import DBCon, DBCur
from SQLite.DBOperation import select_from_table
import csv


# 可以输入股票名称或股票代码，返回股票ts_code,输入错误则返回None
def find_ts_code(name_or_code: str):
    if name_or_code.isdigit():
        result = select_from_table('select ts_code from stock_basic where symbol =\'' + name_or_code + '\'')

    else:
        result = select_from_table('select ts_code from stock_basic where name =\'' + name_or_code + '\'')
    if not len(result) == 0:
        ts_code = result[0][0]
        return ts_code
    else:
        return ''


def create_csv_file(ts_code):
    trade_date, high, low, close, pct_cgh, vol, turnover, volume_ratio, pe, sm_amount, md_amount, lg_amount, elg_amount, net_mf_amount = [], [], [], [], [], [], [], [], [], [], [], [], [], []
    if ts_code == '':
        return
    data = select_from_table(
        'select daily.trade_date,daily.high,daily.low,daily.close,daily.pct_chg,daily.vol,daily_basic.turnover_rate,daily_basic.volume_ratio,daily_basic.pe,round(moneyflow.buy_sm_amount - moneyflow.sell_sm_amount,2) as sm_amount,round(moneyflow.buy_md_amount - moneyflow.sell_md_amount,2) as md_amount,round(moneyflow.buy_lg_amount - moneyflow.sell_lg_amount,2) as lg_amount,round(moneyflow.buy_elg_amount - moneyflow.sell_elg_amount,2) as elg_amount,moneyflow.net_mf_amount from daily,daily_basic,moneyflow where daily.ts_code = daily_basic.ts_code  and daily.trade_date = daily_basic.trade_date and daily.ts_code = moneyflow.ts_code and  daily.trade_date = moneyflow.trade_date and daily.ts_code=\'' + ts_code + '\'')

    for day in data:
        trade_date.append(day[0])
        high.append(day[1])
        low.append(day[2])
        close.append(day[3])
        pct_cgh.append(day[4])
        vol.append(day[5])
        turnover.append(day[6])
        volume_ratio.append(day[7])
        pe.append(day[8])
        sm_amount.append(day[9])
        md_amount.append((day[10]))
        lg_amount.append(day[11])
        elg_amount.append(day[12])
        net_mf_amount.append(day[13])

    df = pd.DataFrame(
        {'交易日期': trade_date, '最高价': high, '最低价': low, '收盘价': close, '涨幅': pct_cgh, '成交量': vol, '换手率': turnover,
         '量比': volume_ratio, '市盈率': pe, '小单净买入': sm_amount, '中单净买入': md_amount, '大单净买入': lg_amount,
         '超大单净买入': elg_amount, '净流入额': net_mf_amount})

    df.to_csv('.//csv//'+ts_code[0:6] + '.csv', index=False, sep=',')


# create_csv_file('000001.SZ')
#