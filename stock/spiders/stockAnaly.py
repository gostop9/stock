# -*- coding: utf-8 -*-
import time
import datetime
import requests
import scrapy
import json
import urllib.parse
from stock.items import StockItem
from lxml import etree

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

#//*[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/div
#//*[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/div
#//*[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/div/a
#//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[1]/div
#//*[@id="qinfo"]/div[1]/div/div[4]/div/span
#http://www.iwencai.com/stockpick/search?w=%E6%9C%BA%E6%9E%84%E5%8A%A8%E5%90%91%EF%BC%8C%E8%82%A1%E6%80%A7%E8%AF%84%E5%88%86%EF%BC%8C%E5%A4%A7%E5%8D%95%E4%B9%B0%E5%85%A5%E6%AF%94%E5%A4%A7%E4%BA%8E%E5%A4%A7%E5%8D%95%E5%8D%96%E5%87%BA%E6%AF%94%EF%BC%8C%E4%B8%BB%E5%8A%A8%E4%B9%B0%E5%85%A5%E6%AF%94%E5%A4%A7%E4%BA%8E%E4%B8%BB%E5%8A%A8%E5%8D%96%E5%87%BA%E6%AF%94&tid=stockpick&qs=stockpick_h&querytype=stock

def saveFile(fileName, content):
    fp = open(fileName, 'w')
    fp.write(content)
    fp.close()
def choose_zhuDongMaiBi(elem):
    return elem[8] #主动买卖比差
    
def attrStrCmp(s):
    if s.find('现价(元)') != -1:
        return '现价'
    if s.find(u'涨跌幅(%)') != -1:
        return '涨跌幅'
    if s.find(u'主力资金流向(元)') != -1:
        return '主力资金流向'
    if s.find(u'dde大单净额(元)') != -1:
        return 'dde大单净额'        
    #if s.find(u'a股流通市值(元)') != -1:
    #    return 'a股流通市值'
    if s.find(u'量比') != -1:
        return '量比'
    if (s == '换手率(%)'):
        return '换手率'
    if s.find(u'dde大单净量(%)') != -1:
        return 'dde大单净量'  
    if s.find(u'机构动向(%)') != -1:
        return '机构动向'
    if s.find(u'中单净额(元)') != -1:
        return '中单净额'
    if s.find(u'主力买入金额(元)') != -1:
        return '主力买入金额'
    if s.find(u'主力卖出金额(元)') != -1:
        return '主力卖出金额'        
    if s.find(u'dde大单买入金额(元)') != -1:
        return 'dde大单买入金额'
    if s.find(u'dde大单卖出金额(元)') != -1:
        return 'dde大单卖出金额'
    if s.find(u'总市值(元)') != -1:
        return '总市值'
    if s.find(u'a股流通市值') != -1:
        return 'a股流通市值'
    if s.find(u'所属同花顺行业') != -1:
        return '所属同花顺行业'  
    if s.find(u'成交额(元)') != -1:
        return '成交额'
    if s.find(u'振幅(%)') != -1:
        return '振幅'
    if s.find(u'大单买入比(%)') != -1:
        return '大单买入比'
    if s.find(u'大单卖出比(%)') != -1:
        return '大单卖出比'        
    if s.find(u'主动买入比(%)') != -1:
        return '主动买入比'
    if s.find(u'主动卖出比(%)') != -1:
        return '主动卖出比'
    if s.find(u'被动买入比(%)') != -1:
        return '被动买入比'
    if s.find(u'被动卖出比(%)') != -1:
        return '被动卖出比'  
    if s.find(u'涨跌幅:前复权(%)') != -1:
        return '涨跌幅前复权'
    if s.find(u'涨跌(元)') != -1:
        return '涨跌'
    if s.find(u'成交量(股)') != -1:
        return '成交量'
    if s.find(u'中单买入金额(元)') != -1:
        return '中单买入金额'        
    if s.find(u'中单卖出金额(元)') != -1:
        return '中单卖出金额'
    if s.find(u'上市天数(天)') != -1:
        return '上市天数'
    if s.find(u'小单净额(元)') != -1:
        return '小单净额'
    if s.find(u'净利润(元)') != -1:
        return '净利润'  
    if s.find(u'净利润同比增长率(%)') != -1:
        return '净利润同比增长率'
    if s.find(u'归属母公司股东的净利润(同比增长率)(%)') != -1:
        return '净利润同比增长率'
    if s.find(u'买入信号') != -1:
        return '买入信号'
    if s.find(u'股性评分') != -1:
        return '股性评分'
    if s.find(u'分时成交量(股)') != -1:
        return '分时成交量'
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
    if (s == '分时换手率(%)'):
        return '分时换手率'  
    if s.find(u'分时涨跌幅:前复权(%)') != -1:
        return '分时涨跌幅前复权'  
    if s.find(u'分时收盘价:不复权(元)') != -1:
        return '分时收盘价不复权'
    if s.find(u'dde大单净流入量(股)') != -1:
        return 'dde大单净流入量'  
    if s.find(u'销售毛利率(%)') != -1:
        return '销售毛利率'  
    if s.find(u'摊薄净资产收益率(%)') != -1:
        return '摊薄净资产收益率'  
    if s.find(u'每股净资产(元)') != -1:
        return '每股净资产'
    if s.find(u'开盘价:不复权(元)') != -1:
        return '开盘价不复权'
    if s.find(u'收盘价:不复权(元)') != -1:
        return '收盘价不复权'
    if s.find(u'最高价:不复权(元)') != -1:
        return '最高价不复权'
    if s.find(u'最低价:不复权(元)') != -1:
        return '最低价不复权'
    if s.find(u'开盘价:前复权(元)') != -1:
        return '开盘价前复权'
    if s.find(u'最高价:前复权(元)') != -1:
        return '最高价前复权'
    if s.find(u'最低价:前复权(元)') != -1:
        return '最低价前复权'
    if s.find(u'收盘价:前复权(元)') != -1:
        return '收盘价前复权'  
    if s.find(u'消息面评分(分)') != -1:
        return '消息面评分'       
    if s.find(u'技术面评分(分)') != -1:
        return '技术面评分'       
    if s.find(u'资金面评分(分)') != -1:
        return '资金面评分'       
    if s.find(u'行业面评分(分)') != -1:
        return '行业面评分'       
    if s.find(u'基本面评分(分)') != -1:
        return '基本面评分'       
    if s.find(u'牛叉诊股综合评分(分)') != -1:
        return '牛叉诊股综合评分'       
    if s.find(u'市日期') != -1:
        return '上市日期'
    if s.find(u'平均成本(元)') != -1:
        return '平均成本'
    if s.find(u'收盘获利(%)') != -1:
        return '收盘获利'
    if s.find(u'集中度70(%)') != -1:
        return '集中度70'
    if s.find(u'集中度90(%)') != -1:
        return '集中度90'
    if s.find(u'外盘成交量(股)') != -1:
        return '外盘成交量'
    if s.find(u'内盘成交量(股)') != -1:
        return '内盘成交量'
    if (s == '自由流通市值(元)'):
        return '自由流通市值'
    if (s == '自由流通股(股)'):
        return '自由流通股'
    if (s == '实际换手率(%)'):
        return '实际换手率'
    else:
        return '其它'
    
        
class StockanalySpider(scrapy.Spider):
    name = 'stockAnaly'
    headers={
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        #'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        #'Cookie':'cid=nskbfvr9pc29m4mjtsdeit4jf31510283024; ComputerID=nskbfvr9pc29m4mjtsdeit4jf31510283024; guideState=1; other_uid=Ths_iwencai_Xuangu_b9b3a6b974ef2a54915c94512d5b3719; PHPSESSID=4cf5e5ab98be906203372c16ab5a17de; v=AlTVo_lY8xjlpGdUEaCtTgtMJZnDrXjcutEM2-404F9i2fqNFr1IJwrh3G09',
        'Host':'www.iwencai.com',
        #'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'hexin-v':'AgeGyk75FjoVzpK2-tJS1FPFlrDSDNtJNeNfYtn0Ixa9SCmm4dxrPkWw77jq'
    }
    #formatStr = "主力净量，主力金额，换手率小于10，量比，大单买入比大于大单卖出比，主动买入比大于主动卖出比，大单净额，中单净额，小单净额，\
    #净利润，净利润增长率，买入信号，股性评分，机构动向，外盘，内盘，总金额，总手，\
    #开盘，昨收，最高，最低，振幅，流通市值，五日线，十日线，二十日线，昨日收盘价低于五日均线，现价高于五日均线".encode('utf-8')
    
    #formatStr = "自由流通市值".encode('utf-8')
    #formatStr = "主力净量，现价，涨跌幅，涨跌，主力金额，换手率，量比，成交量，流通市值，自由流通市值，自由流通股，实际换手率，股性评分，机构动向，大单买入比，大单卖出比，主动买入比，主动卖出比，被动买入比，被动卖出比，大单净额，中单净额，小单净额，成交额，总金额，总市值，总手，开盘价，昨日收盘价，最高价，最低价，振幅，五日线，十日线，二十日线，大单净流入量，流通a股，散户数量，主力买入金额，主力卖出金额，大单买入金额，大单卖出金额，中单买入金额，中单卖出金额，小单买入金额，小单卖出金额，净利润，净利润增长率，所属同花顺行业，上市天数，买入信号，技术形态，选股动向，消息面评分，技术面评分，资金面评分，行业面评分，基本面评分，牛叉诊股综合评分，营业收入，营业收入同比增长率，销售毛利率，摊薄净资产收益率，每股净资产，上市日期".encode('utf-8')
    formatStr = "主力净量，现价，涨跌幅，涨跌，主力金额，换手率，量比，成交量，流通市值，自由流通市值，自由流通股，实际换手率，股性评分，机构动向，大单买入比，大单卖出比，主动买入比，主动卖出比，被动买入比，被动卖出比，大单净额，中单净额，小单净额，成交额，总金额，总市值，总手，开盘价，昨日收盘价，最高价，最低价，振幅，五日线，十日线，二十日线，大单净流入量，流通a股，散户数量，主力买入金额，主力卖出金额，大单买入金额，大单卖出金额，中单买入金额，中单卖出金额，小单买入金额，小单卖出金额，净利润，净利润增长率".encode('utf-8')
    '''
    formatStr = "主力净量，主力金额，换手率小于10，量比，大单买入比，大单卖出比，主动买入比，主动卖出比，大单净额，中单净额，小单净额".encode('utf-8')
    '''
    querystring = {
        'w':formatStr,
        'tid':'stockpick',
        'qs':'stockpick_h',
        'querytype':'stock',
        'p':'1',
        'perpage':'3700',
        'changeperpage':'1'
    }
    cookies = {
        'cid':'nskbfvr9pc29m4mjtsdeit4jf31510283024',
        'ComputerID':'nskbfvr9pc29m4mjtsdeit4jf31510283024',
        #'guideState':'1',
        'other_uid':'Ths_iwencai_Xuangu_b9b3a6b974ef2a54915c94512d5b3719',
        'user':'MDptb18yNTI0MjY2MjM6Ok5vbmU6NTAwOjI2MjQyNjYyMzo1LDEsNDA7NiwxLDQwOzcsMTExMTExMTExMTEwLDQwOzgsMTExMTAxMTEwMDAwMTExMTEwMDEwMDEwMDEwLDQwOzMzLDAwMDEwMDAwMDAwMCwyODE7MzYsMTAwMTExMTEwMDAwMTEwMDEwMTExMTExLDI4MTs0NiwwMDAwMTEwMDEwMDAwMDExMTExMTExMTEsMjgxOzUxLDExMDAwMDAwMDAwMDAwMDAsMjgxOzU4LDAwMDAwMDAwMDAwMDAwMDAxLDI4MTs3OCwxLDI4MTs4NywwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAsMjgxOzQ0LDExLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOjI0Ojo6MjUyNDI2NjIzOjE1NDM1NDkxOTQ6OjoxNDMyNDYwODIwOjQwMDgwNjowOjFlOTNmZDFjNzkwZjY0ODlhNmI4YmY5MTY2M2IyODZkYjpkZWZhdWx0XzI6MQ%3D%3D',
        'userid':'252426623',
        'u_name':'mo_252426623',
        'escapename':'mo_252426623',
        'ticket':'7197fceb268431d3bad66ce1704b645b',
        'PHPSESSID':'bbc2ece0356a87571a88028db40d6ba1',
        'v':'AooLwdMu4ss8WG5nSKqpA4Io23svew6BAPyCeRTDNl1oxyQt_Ate5dCP0oDn'
    }
    
    start_urls = ['http://www.iwencai.com/stockpick/search']
    
    def start_requests(self):
        for url in self.start_urls:
            
            yield scrapy.FormRequest(
                url=url, 
                headers=self.headers, 
                cookies=self.cookies,
                method = 'GET',
                meta={},
                formdata=self.querystring, 
                callback=self.parse,
                errback = self.error,
                dont_filter = True
            )
   

    def parse(self, response):
        #with open("stock.txt", "w") as f:
            #f.write(response.text)
            #//div[@class ='em graph alignCenter']/a
        #a_list = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[2]/div/table/tr[1]/td[3]/div')
        '''
        te = open("D:/Works/PycharmProjects/stock/view-source.txt", 'rt', encoding='UTF8')
        file_text = te.read()        
        te.close()
        response = response.replace(body = file_text)
        '''
        item = StockItem()
        nodeList = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[1]/ul/li')
        
        retryCount = 0
        if(len(nodeList) == 0): #没有抓取到数据
            time.sleep(1)
            retryCount = retryCount + 1;
            '''
            yield scrapy.FormRequest(
                url = self.start_urls[0], 
                headers = self.headers, 
                cookies = self.cookies,
                method = 'GET',
                meta={},
                formdata = self.querystring, 
                callback = self.parse,
                errback = self.error,
                dont_filter = True
            )
            '''
        else:
            #attrList = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[1]/ul/li/div[starts-with(@class,"em")]').extract()
                                      #//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[1]/ul/li[30]/dl/dt/div/span[1]
            #item['code'] = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[2]/div/div/ul/li[3]/div/text()').extract()                                       
            #item['name'] = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[2]/div/div/ul/li[4]/div/text()').extract()
            
            start = time.clock()
            
            #testList = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[*]')
            #text = '/td[{1}]/div/'
            #test11 = testList.xpath(text+'a/text()' + '|' + text+'text()' + '|' + text+'span[1]/text()').extract()
            
            
            end = time.clock()
            print (str(end-start) + '\n')
            start = end

            item['minLen'] = 10000
            item['code'] = response.xpath('//div[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[*]/td[3]/div/text()').extract()
            end = time.clock()
            print (str(end-start) + '\n')
            start = end
            item['name'] = response.xpath('//div[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[*]/td[4]/div/a/text()').extract()
            end = time.clock()
            print (str(end-start) + '\n')
            start = end
            
            col = 1
            for node in nodeList:
                colNum = 0
                if(len(node.xpath('./dl'))): #如果是分列的
                    colNum = len(node.xpath('./dl/dd')) - 1
                    if(len(node.xpath('./dl/dt/div/span'))):
                        attr = node.xpath('./dl/dt/div/span[1]/text()').extract()[0]
                    else:
                        attr = node.xpath('./dl/dt/div/text()').extract()[0]
                else:
                    if(len(node.xpath('./div[1]/span'))): #有解释
                        attr = node.xpath('./div[1]/span[1]/text()').extract()[0]
                    else:
                        attr = node.xpath('./div[1]/text()').extract()[0]
                        
                end = time.clock()
                print (str(end-start) + '\n')
                start = end
                
                string = attrStrCmp(attr)
                print(attr + ' ')
                print(string+ '\n')
                #print(type(attr), len(attr))
                #print(type(string), len(string))

                text = '//div[@class="scroll_tbody_con"]/table/tbody/tr[*]/td[{:d}]/div/'.format(col)
                '''
                ddd  = response.xpath(text+'a')
                if(len(response.xpath(text+'a'))):#有链接
                    item[string] = response.xpath(text+'a/text()').extract()
                else:
                    item[string] = response.xpath(text+'text()').extract()
                '''
                item[string] = response.xpath(text+'a/text()' + '|' + text+'text()' + '|' + text+'span[1]/text()').extract()
                col = col + 1 + colNum
                end = time.clock()
                print (str(end-start) + '\n')
                start = end

                item['minLen'] = min(item['minLen'], len(item[string]))
            
            now = datetime.datetime.now()
            fileStr = now.strftime('%Y%m%d')
            fileName = 'D:/share/自由流通市值_' + fileStr + '.txt'
            self.f = open(fileName, "w")
            for i in range(len(item['code'])):
                self.f.write(item['code'][i] + ' ' + item['name'][i] + ' ' + item['自由流通股'][i] + ' ' + item['股性评分'][i] + '\n')
            self.f.write('\n')
            self.f.close()
            '''
            self.f = open("D:/share/result11.txt", "a+")
            print(len(item['code']))
            for i in range(len(item['code'])):
                self.f.write(item['code'][i] + '\n')
            print(len(item['name']))
            for i in range(len(item['name'])):
                self.f.write(item['name'][i] + '\n')
            print(len(item['liuTongShiZhi']))
            for i in range(len(item['liuTongShiZhi'])):
                self.f.write(item['liuTongShiZhi'][i] + '\n')
            self.f.close()

            lists = []
            for i in range(len(item['code'])):
                
                #list = [item['code'][i], item['name'][i], item['股流通市值'][i], item['大单净量'][i], item['换手率'][i], item['涨跌幅'][i], item['量比'][i], \
                #item['现价'][i], item['振幅'][i], item['机构动向'][i], item['股性评分'][i], item['大单净额'][i], item['主力资金流向'][i], item['中单净额'][i], \
                #item['小单净额'][i], item['净利润同比增长率'][i], item['净利润'][i]]
                
                list = []
                list.append(item['code'][i])
                list.append(item['name'][i])
                list.append(item['liuTongShiZhi'][i])
                list.append(item['大单净量'][i])
                list.append(item['换手率'][i])
                list.append(item['涨跌幅'][i])
                list.append(item['量比'][i])
                list.append(item['现价'][i])
                list.append(float(item['主动买入比'][i]) - float(item['主动卖出比'][i]))
                list.append(float(item['大单买入比'][i]) - float(item['大单卖出比'][i]))
                list.append(item['振幅'][i]) #10
                list.append(item['机构动向'][i])
                list.append(item['股性评分'][i])
                list.append(item['大单净额'][i])
                list.append(item['主力资金流向'][i])
                list.append(item['中单净额'][i])
                list.append(item['小单净额'][i])
                #list.append(item['净利润同比增长率'][i])            
                list.append(item['净利润'][i])
                #
                lists.append(list)
            lists.sort(key = choose_zhuDongMaiBi, reverse = True)    
            
            print(str(len(item['code']))+'\n')
            print(str(len(item['name']))+'\n')
            print(str(len(item['a股流通市值']))+'\n')
            print(str(len(item['dde大单净量']))+'\n')
            print(str(len(item['换手率']))+'\n')
            print(str(len(item['涨跌幅前复权']))+'\n')
            print(str(len(item['量比']))+'\n')
            #print(str(len(item['现价']))+'\n')
            print(str(len(item['主动买入比']))+'\n')
            print(str(len(item['主动卖出比']))+'\n')
            print(str(len(item['振幅']))+'\n')
            print(str(len(item['机构动向']))+'\n')
            print(str(len(item['股性评分']))+'\n')
            print(str(len(item['dde大单净额']))+'\n')
            print(str(len(item['主力资金流向']))+'\n')
            print(str(len(item['中单净额']))+'\n')
            print(str(len(item['小单净额']))+'\n')
            print(str(len(item['净利润同比增长率']))+'\n')
            print(str(len(item['净利润']))+'\nyield\n')
            '''
            yield item            
            
            i = 1
        
    def error(self, response):
        i = 2
        pass
