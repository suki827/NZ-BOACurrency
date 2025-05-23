
import time
from datetime import datetime

from boc.getcurrencydata import main
from boc.sentEmail import send_email
from data.sqlsite import SQLiteDB

if __name__ == "__main__":
    global c_name, c_value
    best_value = 0
    previous_c_value = None
    Threshol = 4.27

    while True:
        db = SQLiteDB(db_name='currency.db', db_dir='./data')
        # 获取当前日期和时间
        current_datetime = datetime.now()
        datetime = current_datetime.replace(microsecond=0)

        # 格式化输出
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Current Date and Time:", formatted_datetime)

        result = main()
        if result:
            c_name, c_value = result['c_name'], result['c_value']
            c_value = float(c_value)
            c_value = f"{c_value:.4f}"

        # insert data to database
        db.insert_data("INSERT INTO currency (c_name, c_value, date) VALUES (?, ?, ?)",
                       (c_name, c_value, datetime))
        db.close()
        if previous_c_value is not None:
            print(f'previous_c_value:', previous_c_value)
            print(f'current_value:',c_value)
            print('Threshold:', float(previous_c_value) - float(c_value))
        # 如果previous_c_value有值，进行0.01的比较
        if previous_c_value is not None and (round(float(previous_c_value), 2) - round(float(c_value),2)) >= 0.01:
            # print(f"{c_name} 的值下降了 0.01，当前值为: {c_value}")
            message = f'Time:{formatted_datetime},---Currency is {c_value}'

            # 发送邮件
            body = message
            recipient_email1 = 'hugo.huan@outlook.com'

            # 调用函数发送邮件
            send_email(body, recipient_email1)


        # 更新previous_c_value为当前c_value
        previous_c_value = c_value

        time.sleep(120)