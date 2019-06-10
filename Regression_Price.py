import matplotlib.pyplot as plt
import numpy as np
import requests
from sklearn.linear_model import LinearRegression

from twstock import Stock


def get_proxy_all():
    try:
        response = requests.get('http://127.0.0.1:5010/get_all')
        # print(response)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        return None



ip_list =get_proxy_all()
time = []
ip = ip_list[0]
stock_prices = Stock(ip,'1101').price #越後面的是越新的
print(stock_prices)
i=0
for stock_price in stock_prices :
    time.append(i)
    i = i+1

print(time)


temperatures = np.array(time)
iced_tea_sales = np.array(stock_prices)

lm = LinearRegression()
lm.fit(np.reshape(temperatures, (len(temperatures), 1)), np.reshape(iced_tea_sales, (len(iced_tea_sales), 1)))

# 新的氣溫
to_be_predicted = np.array([31])
predicted_sales = lm.predict(np.reshape(to_be_predicted, (len(to_be_predicted), 1)))


print(predicted_sales)
# 視覺化
plt.scatter(temperatures, iced_tea_sales, color='black')
plt.plot(temperatures, lm.predict(np.reshape(temperatures, (len(temperatures), 1))), color='blue', linewidth=3)
plt.plot(to_be_predicted, predicted_sales, color = 'red', marker = '^', markersize = 10)
plt.xticks(())
plt.yticks(())
plt.show()