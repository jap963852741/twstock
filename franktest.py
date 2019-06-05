from time import sleep

import twstock
import os, sys
import subprocess
from subprocess import PIPE
import googlesheet_frank
import crawler_yahoostock
from twstock import Stock, BestFourPoint
# import requests
#
# PROXY_POOL_URL = 'http://localhost:5000/get'
#
# def get_proxy():
#     try:
#         response = requests.get(PROXY_POOL_URL)
#         if response.status_code == 200:
#             return response.text
#     except ConnectionError:
#         return None

# print(get_proxy())



# twstock.__update_codes()
stocklist = []
The_Net_Asset_Value = []
EPS = []
Debt_Asset_ratio = []
ROE =[]
Dividend_Payout_Ratio=[]
Tradin_volume=[]
Now_Tradin_volume= []
Establishment_time=[]
buy_sell_point=[]
######################## 年更新#############################################################
# for item in twstock.stock_twse.keys(): #成立時間
#     a= crawler_yahoostock.get_Establishment_time(item)
#     i = a
#     Establishment_time.append(i)
# googlesheet_frank.The_Establishment_time_information().write(Establishment_time)
######################## 年更新#############################################################
# for item in twstock.stock_twse.keys(): #EPS寫入
#     a= crawler_yahoostock.get_EPS(item)
#     i = item+","+a
#     EPS.append(i)
# googlesheet_frank.The_EPSinformation().write(EPS)
######################### 年更新#############################################################

# for item in twstock.stock_twse.keys(): #每股淨值寫入
#     i = item+" "+crawler_yahoostock.get_The_Net_Asset_Value(item)
#     The_Net_Asset_Value.append(i)
# googlesheet_frank.The_Net_Asset_Valueinformation().write(The_Net_Asset_Value)

######################## 年更新#############################################################




######################## 季更新#############################################################
#
# for item in twstock.stock_twse.keys(): #負債資產比
#     try:
#         i = crawler_yahoostock.get_Debt_Asset_ratio(item)
#     except:
#         i = item
#     print(i)
#     Debt_Asset_ratio.append(i)
# googlesheet_frank.The_Debt_Asset_ratio_information().write(Debt_Asset_ratio)
#
# for item in twstock.stock_twse.keys(): #負債資產比
#     try:
#         i = crawler_yahoostock.get_ROE(item)
#     except:
#         i = item
#     print(i)
#     ROE.append(i)
# googlesheet_frank.The_ROE_information().write(ROE)
# #
# for item in twstock.stock_twse.keys(): #負債資產比
#     try:
#         i = crawler_yahoostock.get_Dividend_Payout_Ratio(item)
#     except:
#         i = item
#     print(i)
#     Dividend_Payout_Ratio.append(i)
# googlesheet_frank.The_Dividend_Payout_Ratio_information().write(Dividend_Payout_Ratio)


######################## 季更新#############################################################





######################## 日更新#############################################################

#
for item in twstock.stock_twse.keys():
    # stdout,process = subprocess.Popen("twstock -b {}".format(item), stdout=subprocess.PIPE, stderr=PIPE, stdin=subprocess.PIPE, shell=True).communicate()
    # print(stdout.decode('utf-8'))
    stock = Stock(item)
    try:
        bfp = BestFourPoint(stock)
        result = bfp.best_four_point()
        # print(bfp.best_four_point())
        if result[0] == 'True' :  # 判斷是否為四大買點
            print(item+',buy'+result[1])
        else :        # print(bfp.best_four_point()[1])
            print(item+',sell'+result[1])

        bfp.best_four_point_to_sell()  # 判斷是否為四大賣點
        bfp.best_four_point()
        buy_sell_point.append(bfp.best_four_point())
    except:
        pass
    # bfp.__del__()

    # buy_sell_point.append(stdout.decode('utf-8'))
googlesheet_frank.The_Buy_Sell_Point_information().write(buy_sell_point)













#
# for item in twstock.stock_twse.keys(): #即時交易量
#     try:
#         i = crawler_yahoostock.get_Now_Tradin_volume(item)
#     except:
#         i = item
#     print(i)
#     Now_Tradin_volume.append(i)
# googlesheet_frank.The_Now_Tradin_volume_information().write(Now_Tradin_volume)
#
#
#
# for item in twstock.stock_twse.keys(): #交易量
#     try:
#         i = crawler_yahoostock.get_Tradin_volume(item)
#     except:
#         i = item
#     print(i)
#     Tradin_volume.append(i)
# googlesheet_frank.The_Tradin_volume_information().write(Tradin_volume)
#
#
#
#
#
#



















# stocklist.append('代號')
# for item in twstock.frank_twse.keys(): #上市股票號寫入雲端
#     stocklist.append(item)
#     print(item)
# googlesheet_frank.Googleinformation().write(stocklist)








#     stock = twstock.realtime.get(item) # realtime — 即時股票資訊
#     try :      #accumulate_trade_volume	 累積成交量字串
#         if stock['realtime']['open'] is not None and stock['success']:
#             if float(stock['realtime']['open']) > 20 and float(stock['realtime']['open']) < 40  :
#                 print(stock)
#                 stocknumber.append(item)
#                             # print(str(stock['info']['name']))
#                 print("%s \n%s%s %s"%(str(stock['info']['name']),'開盤價',':',str(stock['realtime']['open'])))
#                             # print('盤中最高價 : ' + str(stock['realtime']['high']))   and float(stock['realtime']['trade_volume']) > 100
#                             # print('盤中最低價 : ' + str(stock['realtime']['low']))
#             if float(stock['info']['code']) > 9500 :        #後面都英文字的 open沒東西
#                 break
#     except:
#         pass
#
# print(len(stocknumber))
# print(stocknumber)
















#從以前列到現在
# stock = twstock.Stock('6625',initial_fetch=True)
# stock.fetch_from(2018,10)
# print(stock.data)
# print(stock.ma_bias_ratio(5,10))
# list = []
# for item in stock.data: #上市  從舊到新
#
#     print(str(item[0])+'開盤價 : '+str(item[3]))
#     if item is not None :
#         list.append(item[3])
#     # stock = twstock.realtime.get(item)  # realtime — 即時股票資訊
#     # if stock['success']:
#     #     print(stock)
#     #     print('開盤價 : ' + str(stock['realtime']['open']))
#     #     print('盤中最高價 : ' + str(stock['realtime']['high']))
#     #     print('盤中最低價 : ' + str(stock['realtime']['low']))
#
# print(list)
# print('max : '+str(max(list)))
# print('min : '+str(min(list)))


# bfp = twstock.BestFourPoint( twstock.Stock('6625'))
# print(bfp.best_four_point())



# for item in twstock.twse.keys(): #上市
#     print(item)
#     stock = twstock.realtime.get(item)  # realtime — 即時股票資訊
#     if stock['success']:
#         print(stock)
#         print('開盤價 : ' + str(stock['realtime']['open']))
#         print('盤中最高價 : ' + str(stock['realtime']['high']))
#         print('盤中最低價 : ' + str(stock['realtime']['low']))




# print(stock.moving_average(stock.price, 1))
# stdout,process = subprocess.Popen("twstock -b {}".format('2330'), stdout=subprocess.PIPE, stderr=PIPE, stdin=subprocess.PIPE, shell=True).communicate()
# print(stdout.decode('utf-8'))
# stock.sid
# sidstock.price  #回傳各日之收盤價

# print(stock.sid)

# print(stock.price)


