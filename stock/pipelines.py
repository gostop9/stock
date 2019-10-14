# -*- coding: utf-8 -*-
# change log: 20190909 DDE大单净量、主动卖出比，不能爬取，修改存储内容
import os
import datetime
from operator import itemgetter, attrgetter
import pymongo
from scrapy.conf import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

def list_sub(a, b):
    c = []
    for i in range(len(a)):
        c.append(float(a[i]) - float(b[i]))
    return c
    
def choose_zhuDongMaiBi(elem):
    return elem[8] #主动买卖比差

class StockPipeline(object):
    def __init__(self):
        now = datetime.datetime.now()
        string = now.strftime('%Y%m%d')
        fileName = 'D:/share/wencai_' + string + '.txt'
        #if(os.path.exists(fileName))
        self.fwencai = open(fileName, "a+")
        self.f = open("D:/share/result.txt", "a+")
        
        #数据库
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = 'wencai_' + string
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.client = mydb[sheetname]
        
    def process_item(self, item, spider):
        #item['大单买卖比差'] = list_sub(item['大单买入比'], item['大单卖出比'])
        #item['主动买卖比差'] = list_sub(item['主动买入比'], item['主动卖出比'])
        
        print(item['minLen'])
        
        print(str(len(item['code']))+'\n')
        print(str(len(item['name']))+'\n')
        print(str(len(item['a股流通市值']))+'\n')
        print(str(len(item['主动买入比']))+'\n')
        print(str(len(item['换手率']))+'\n')
        print(str(len(item['涨跌幅前复权']))+'\n')
        print(str(len(item['量比']))+'\n')
        print(str(len(item['收盘价不复权']))+' 收盘价不复权\n')
        print(str(len(item['主动买入比']))+'\n')
        print(str(len(item['被动买入比']))+'\n')
        print(str(len(item['振幅']))+'\n')
        print(str(len(item['机构动向']))+'\n')
        print(str(len(item['股性评分']))+'\n')
        print(str(len(item['dde大单净额']))+'\n')
        print(str(len(item['主力资金流向']))+'\n')
        print(str(len(item['中单净额']))+'\n')
        print(str(len(item['小单净额']))+'\n')
        print(str(len(item['净利润同比增长率']))+'\n')
        print(str(len(item['净利润']))+'\nyield\n')
        
        lists = []
        
        for i in range(item['minLen']):
            '''
            list = [item['code'][i], item['name'][i], item['a股流通市值'][i], item['dde大单净量'][i], item['换手率'][i], item['涨跌幅前复权'][i], item['量比'][i], \
            item['现价'][i], item['振幅'][i], item['机构动向'][i], item['股性评分'][i], item['dde大单净额'][i], item['主力资金流向'][i], item['中单净额'][i], \
            item['小单净额'][i], item['净利润同比增长率'][i], item['净利润'][i]]
            '''
            list = []
            list.append(item['code'][i])
            list.append(item['name'][i])
            list.append(item['a股流通市值'][i])
            list.append(item['主动买入比'][i])
            list.append(item['换手率'][i])
            list.append(item['涨跌幅前复权'][i])
            list.append(item['量比'][i])
            if '现价' in item:
                list.append(item['现价'][i])
            else:
                list.append(item['收盘价不复权'][i])
            #print(item['主动买入比'][i]+' ')
            #print(item['主动卖出比'][i]+'\n')
            list.append(float(item['主动买入比'][i]) - float(item['被动买入比'][i]))
            #list.append(float(item['大单买入比'][i]) - float(item['大单卖出比'][i]))
            list.append(item['振幅'][i]) #9
            list.append(item['机构动向'][i])
            list.append(item['股性评分'][i])
            list.append(item['dde大单净额'][i])
            list.append(item['主力资金流向'][i])
            list.append(item['中单净额'][i])
            list.append(item['小单净额'][i])
            list.append(item['净利润同比增长率'][i])            
            list.append(item['净利润'][i])
            #'''
            lists.append(list)
        
        if (len(lists) > 20):

            mongoData = dict(item)
            self.client.insert(mongoData)
            
            lists.sort(key = itemgetter(8), reverse = True)
            
            self.fwencai.write(str(len(lists)))
            text = '\ncode '+'name '+'a股流通市值 '+'主动买入比 '+'换手率 '+'涨跌幅前复权 '+'量比 '+'现价 '+'主动买卖比差 '+'振幅 '+'机构动向 '+'股性评分 '+'dde大单净额 '+'主力资金流向 '+'中单净额 '+'小单净额 '+'净利润同比增长率 '+'净利润\n'
            self.fwencai.write(text)
            
            for i in range(len(lists)):
                for j in range(len(lists[i])):
                    self.fwencai.write(str(lists[i][j]) + ' ')
                self.fwencai.write('\n')
                if (float(lists[i][3]) >= 0.6) \
                and (float(lists[i][6]) >= 0.9) \
                and (lists[i][8] >= 0.6) \
                and (float(lists[i][10]) >= 9) \
                and (float(lists[i][11]) >= 40):            
                    text = '{:s},{:s}, {:s}, DDE:{:s}, 换:{:s}, 涨:{:s}, 量:{:s}, 价:{:s}, 主比:{:+.2f}, 幅:{:s}, 机:{:s}, 股:{:s}, 大净:{:s}, 主流:{:s}, 中:{:s}, 小:{:s}, 净增:{:s}, 净利:{:s}\n'.format(lists[i][0], lists[i][1], lists[i][2], lists[i][3], lists[i][4], lists[i][5], lists[i][6], lists[i][7], lists[i][8], lists[i][9], lists[i][10], lists[i][11], lists[i][12], lists[i][13], lists[i][14], lists[i][15], lists[i][16], lists[i][17])
                    #text = '{:s},{:s}, {:s}, {:s}, {:s}, {:s}, {:s}, {:s}\n'.format(lists[i][0], lists[i][1], lists[i][2], lists[i][3],, lists[i][4], lists[i][5], lists[i][6], lists[i][7])
                    self.f.write(text)
            self.f.write('\n\n')
            self.fwencai.write('\n')
            
            i=1;
        return item
    
    def close_spider(self, spider):
        self.fwencai.close()
        self.f.close()
        #self.client.close()