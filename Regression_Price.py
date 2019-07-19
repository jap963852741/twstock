import matplotlib.pyplot as plt
import numpy as np
import requests
from sklearn.linear_model import LinearRegression

import googlesheet_frank
from twstock import Stock

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
def get_proxy_all():
    try:
        response = requests.get('http://127.0.0.1:5010/get_all')
        # print(response)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        return None

Regression = []
Point_list = ['1605','1909','2014','2323','2349','2368','2399','2823']
aa=0
ip_list =get_proxy_all()
delete_proxy('111.231.18.136:1080')

for item in Point_list:

    time = []
    ip = ip_list[aa%len(ip_list)]
    stock_prices = Stock(ip,item).price #越後面的是越新的
    print(stock_prices)
    i=0
    for stock_price in stock_prices :
        time.append(i)
        i = i+1
    temperatures = np.array(time)
    iced_tea_sales = np.array(stock_prices)

    lm = LinearRegression()
    try:
        lm.fit(np.reshape(temperatures, (len(temperatures), 1)), np.reshape(iced_tea_sales, (len(iced_tea_sales), 1)))
        to_be_predicted = np.array([31])
        predicted_sales = lm.predict(np.reshape(to_be_predicted, (len(to_be_predicted), 1)))

        print(predicted_sales)
        aa = aa + 1
        Regression.append(item + ',' + str(predicted_sales[0][0]))
    except:
        pass
    # 新的氣溫


googlesheet_frank.Regression_Price_information().write(Regression)






# 視覺化
# plt.scatter(temperatures, iced_tea_sales, color='black')
# plt.plot(temperatures, lm.predict(np.reshape(temperatures, (len(temperatures), 1))), color='blue', linewidth=3)
# plt.plot(to_be_predicted, predicted_sales, color = 'red', marker = '^', markersize = 10)
# plt.xticks(())
# plt.yticks(())
# plt.show()