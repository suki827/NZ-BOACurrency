import os

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from boc.sentEmail import send_email
from data.sqlsite import SQLiteDB
def fetch_exchange_rate(url, currency_name, page=1):
    # 请求参数
    params = {
        'pjname': currency_name,  # 外汇种类，例如 '新西兰元'
        'page': str(page)  # 页码
    }

    # get html content by request
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            # parse  HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            rows = soup.select('.publish table tr')

            # 获取第二个 <tr>（第一个是表头）
            if len(rows) > 1:
                first_row = rows[1]
                f_columns = first_row.find_all('th')
                f_data = [col.text for col in f_columns]
                name, saleValue = f_data[0], f_data[3]
                second_row = rows[18]
                s_columns = second_row.find_all('td')
                for row in rows:
                    colums = row.find_all('td')
                    if len(colums) > 0 and colums[0] == '新西兰元':   s_columns = colums

                s_data = [col.text for col in s_columns]
                nz, value = s_data[0], s_data[3]
                value = float(value) / 100
                return {
                    'c_name': nz,
                    'c_value': value
                }
            else:
                print("no data found")
                return None
        else:
            print("request error，statue_code : {response.status_code}")
            return None
    except Exception as e:
        return e


# main 函数
def main():
    global result
    # URL
    url = "https://www.boc.cn/sourcedb/whpj/index.html"
    url1 = "https://www.boc.cn/sourcedb/whpj/index_1.html"
    currency_name = "新西兰元"

    # 调用函数获取数据
    result = fetch_exchange_rate(url, currency_name)
    if result is not None:
        name, value = result
        if name != "新西兰元":
            result = fetch_exchange_rate(url1, currency_name)
        return result
