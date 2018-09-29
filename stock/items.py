# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # DDE    
    code = scrapy.Field()
    
    name = scrapy.Field()    
    
    ddeIdx = scrapy.Field()
    
    dde大单净量 = scrapy.Field()
    
    huanShou = scrapy.Field()
    
    liangBi = scrapy.Field()
    
    主力资金流向 = scrapy.Field()
    
    涨跌幅 = scrapy.Field()
    
    振幅 = scrapy.Field()
    
    所属同花顺行业 = scrapy.Field()
    
    xingJi = scrapy.Field()
    
    现价 = scrapy.Field()
    
    zhangSu = scrapy.Field()
    
    zongShou = scrapy.Field()
    
    换手率 = scrapy.Field()
    
    量比 = scrapy.Field()
    
    zongJinE = scrapy.Field()
    
    机构动向 = scrapy.Field()
    
    涨跌幅前复权 = scrapy.Field()
    
    涨跌 = scrapy.Field()
    
    成交量 = scrapy.Field()
        
    股性评分 = scrapy.Field()
    
    开盘价不复权 = scrapy.Field()
    收盘价不复权 = scrapy.Field()
    最高价不复权 = scrapy.Field()
    最低价不复权 = scrapy.Field()
    开盘价前复权 = scrapy.Field()
    最高价前复权 = scrapy.Field()
    最低价前复权 = scrapy.Field()
    收盘价前复权 = scrapy.Field()
    # zijin        
    dde大单净额 = scrapy.Field()
    
    中单净额 = scrapy.Field()
    
    主力买入金额 = scrapy.Field()
    
    主力卖出金额 = scrapy.Field()
    
    dde大单买入金额 = scrapy.Field()
    
    dde大单卖出金额 = scrapy.Field()    
    
    dde大单净流入量 = scrapy.Field()
    
    总市值 = scrapy.Field()
    
    a股流通市值 = scrapy.Field()

    成交额 = scrapy.Field()
    
    大单买入比 = scrapy.Field()
    
    大单卖出比 = scrapy.Field()
    
    大单买卖比差 = scrapy.Field()
    
    主动买入比 = scrapy.Field()
    
    主动卖出比 = scrapy.Field()
    
    主动买卖比差 = scrapy.Field()
    
    被动买入比 = scrapy.Field()
    
    被动卖出比 = scrapy.Field()
    
    中单买入金额 = scrapy.Field()

    中单卖出金额 = scrapy.Field()
    
    小单净额 = scrapy.Field()    
    
    小单买入金额 = scrapy.Field()
    
    小单卖出金额 = scrapy.Field()
    
    daDanZongE = scrapy.Field()
    
    daDanZongEB = scrapy.Field()
    
    zhongDanJingEB = scrapy.Field()
    
    zhongDanZongE = scrapy.Field()
    
    zhongDanZongEB = scrapy.Field()
    
    xiaoDanJingEB = scrapy.Field()
    
    xiaoDanZongE = scrapy.Field()
    
    xiaoDanZongEB = scrapy.Field()

    # zhuli    
    分时成交量 = scrapy.Field()
    
    五日均线 = scrapy.Field()
    
    十日均线 = scrapy.Field()
    
    二十日均线 = scrapy.Field()

    
    行情收盘价 = scrapy.Field()
    
    dde散户数量 = scrapy.Field()
    
    流通a股 = scrapy.Field()
    
    #财务   
    上市天数 = scrapy.Field()
    
    净利润 = scrapy.Field()
    
    净利润同比增长率 = scrapy.Field()
    
    买入信号 = scrapy.Field()
    
    营业收入 = scrapy.Field()
    
    营业收入同比增长率 = scrapy.Field()
    
    技术形态 = scrapy.Field()
    
    选股动向 = scrapy.Field()
    
    分时成交额 = scrapy.Field()
    
    分时换手率 = scrapy.Field()
    
    分时涨跌幅前复权 = scrapy.Field()
    
    分时收盘价不复权 = scrapy.Field()
    销售毛利率 = scrapy.Field()
    摊薄净资产收益率 = scrapy.Field()
    每股净资产 = scrapy.Field()
    
    消息面评分 = scrapy.Field()    
    技术面评分 = scrapy.Field()
    资金面评分 = scrapy.Field()
    行业面评分 = scrapy.Field()
    基本面评分 = scrapy.Field()
    牛叉诊股综合评分 = scrapy.Field()
    上市日期 = scrapy.Field()
    平均成本 = scrapy.Field()
    收盘获利 = scrapy.Field()
    集中度70 = scrapy.Field()
    集中度90 = scrapy.Field()
    
    内盘成交量 = scrapy.Field()
    外盘成交量 = scrapy.Field()
    
    自由流通市值 = scrapy.Field()
    自由流通股 = scrapy.Field()
    实际换手率 = scrapy.Field()
    
    其它 = scrapy.Field()
    minLen = scrapy.Field()
    pass

'''    
def attrStrCmp(s):
    if s.find('现价(元)') != -1:
        return 'xianJia'
    if s.find(u'涨跌幅(%)') != -1:
        return 'zhangFu'
    if s.find(u'主力资金流向(元)') != -1:
        return 'zhuLiJinE'
    if s.find(u'dde大单净额(元)') != -1:
        return 'daDanJingE'        
    if s.find(u'a股流通市值(元)') != -1:
        return 'liuTongShiZhi'
    if s.find(u'量比') != -1:
        return 'liangBi'
    if s.find(u'换手率(%)') != -1:
        return 'huanShou'
    if s.find(u'dde大单净量(%)') != -1:
        return 'dde'  
    if s.find(u'机构动向(%)') != -1:
        return 'jiGouDongXiang'
    if s.find(u'中单净额(元)') != -1:
        return 'zhongDanJingE'
    if s.find(u'主力买入金额(元)') != -1:
        return 'zhuLiRuJinE'
    if s.find(u'主力卖出金额(元)') != -1:
        return 'zhuLiChuJinE'        
    if s.find(u'dde大单买入金额(元)') != -1:
        return 'ddeRuJinE'
    if s.find(u'dde大单卖出金额(元)') != -1:
        return 'ddeChuJinE'
    if s.find(u'总市值(元)') != -1:
        return 'zongShiZhi'
    if s.find(u'a股流通市值') != -1:
        return 'a股流通市值'
    if s.find(u'所属同花顺行业') != -1:
        return 'suoShuHangYe'  
    if s.find(u'成交额(元)') != -1:
        return 'chengJiaoE'
    if s.find(u'振幅(%)') != -1:
        return 'zhenFu'
    if s.find(u'大单买入比(%)') != -1:
        return 'DaDanRuBi'
    if s.find(u'大单卖出比(%)') != -1:
        return 'daDanChuBi'        
    if s.find(u'主动买入比(%)') != -1:
        return 'zhuDongRuBi'
    if s.find(u'主动卖出比(%)') != -1:
        return 'zhuDongChuBi'
    if s.find(u'被动买入比(%)') != -1:
        return 'beiDongRuBi'
    if s.find(u'被动卖出比(%)') != -1:
        return 'beiDongChuBi'  
    if s.find(u'涨跌幅:前复权(%)') != -1:
        return 'zhangDieFuFuQuan'
    if s.find(u'涨跌(元)') != -1:
        return 'zhangDie'
    if s.find(u'成交量(股)') != -1:
        return 'chengJiaoLiang'
    if s.find(u'中单买入金额(元)') != -1:
        return 'zhongDanRuJinE'        
    if s.find(u'中单卖出金额(元)') != -1:
        return 'zhongDanChuJinE'
    if s.find(u'上市天数(天)') != -1:
        return 'shangShiTianShu'
    if s.find(u'小单净额(元)') != -1:
        return 'xiaoDanJingE'
    if s.find(u'净利润(元)') != -1:
        return 'jingLiRun'  
    if s.find(u'净利润同比增长率(%)') != -1:
        return 'jingLiZengZhang'
    if s.find(u'买入信号') != -1:
        return 'maiRuXinHao'
    if s.find(u'股性评分') != -1:
        return 'guXingPingFen'
    if s.find(u'分时成交量(股)') != -1:
        return 'fenShiChengJiaoLiang'
    if s.find(u'5日均线') != -1:
        return '五日均线'        
    if s.find(u'10日均线') != -1:
        return '十日均线'
    if s.find(u'20日均线') != -1:
        return '二十日均线'
    if s.find(u'行情收盘价') != -1:
        return '行情收盘价'  
    if s.find(u'dde散户数量') != -1:
        return 'dde散户数量'  
    if s.find(u'流通a股(股)') != -1:
        return '流通a股'  
    if s.find(u'小单买入金额(元)') != -1:
        return '小单买入金额'  
    if s.find(u'小单卖出金额(元)') != -1:
        return '小单卖出金额'  
    if s.find(u'营业收入(元)') != -1:
        return '营业收入'  
    if s.find(u'营业收入(同比增长率)(%)') != -1:
        return '营业收入同比增长率'  
    if s.find(u'技术形态') != -1:
        return '技术形态'  
    if s.find(u'选股动向') != -1:
        return '选股动向'  
    if s.find(u'分时成交额(元)') != -1:
        return '分时成交额'  
    if s.find(u'分时换手率(%)') != -1:
        return '分时换手率'  
    if s.find(u'分时涨跌幅:前复权(%)') != -1:
        return '分时涨跌幅前复权'  
    if s.find(u'分时收盘价:不复权(元)') != -1:
        return '分时收盘价不复权'  
    if s.find(u'消息面评分(分)') != -1:
        return '消息面评分'  
    if s.find(u'dde大单净流入量(股)') != -1:
        return 'dde大单净流入量'  
    if s.find(u'销售毛利率(%)') != -1:
        return '销售毛利率'  
    if s.find(u'摊薄净资产收益率(%)') != -1:
        return '摊薄净资产收益率'  
    if s.find(u'每股净资产(元)') != -1:
        return '每股净资产'
'''