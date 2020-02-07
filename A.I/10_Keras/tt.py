import requests
import bs4
import pandas as pd
import time

price_url = 'https://fchart.stock.naver.com/sise.nhn?symbol=KOSPI&timeframe=day&count=1500&requestType=0'
price_data = requests.get(price_url)
# print(price_data)

price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml')
# print(price_data_bs)

item_list = price_data_bs.find_all('item')
# print(item_list)

temp = item_list[0]['data']
temp.split('|')
# print(temp)

for item in item_list:
    temp_data = item['data']
    datas = temp_data.split('|')
    print(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5])