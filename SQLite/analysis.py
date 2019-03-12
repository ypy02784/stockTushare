#coding = utf-8
import time


_NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  #默认系统当前日期

#获取龙虎榜中涨的股票SELECT DISTINCT(ts_code),top_list.`name`,pct_change,turnover_rate,amount,l_amount,net_amount,amount_rate  from top_list where trade_date ='20190311' and net_amount >0 and turnover_rate <10 and pct_change >0
def get_top_list_rise_stock(tradedate=_NOWTIME,pct_change=0,turnover_rate=10,netamount=0):
    sql = 'SELECT DISTINCT( ts_code ) AS 股票代码,top_list.`name` AS 股票名称,pct_change AS 涨跌 ,turnover_rate AS 换手率,amount AS 交易额, l_amount AS 龙虎榜交易额,net_amount AS 龙虎榜净买入,amount_rate AS 龙虎榜占比 FROM top_list WHERE trade_date = \''+tradedate+'\''
    sql = sql + ' AND net_amount > '+str(netamount)+' AND turnover_rate < '+str(turnover_rate)+'AND pct_change >'+str(pct_change)
    print(sql)


get_top_list_rise_stock(pct_change=5)