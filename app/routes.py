import json

from flask import Blueprint, jsonify
from datetime import datetime

from data.sqlsite import SQLiteDB

# 创建一个蓝图（Blueprint）
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    db = SQLiteDB(db_name='currency.db')
    # 获取当前日期和时间
    current_datetime = datetime.now()

    # 格式化输出
    formatted_current_datetime = current_datetime.strftime("%Y-%m-%d %H")
    print(f'查询时间为{formatted_current_datetime}')
    query_sql = """
    SELECT *
    FROM currency 
    WHERE strftime('%Y-%m-%d %H', date) = ?
    order by id desc limit 1"""

    res = db.query_data(query_sql,(formatted_current_datetime,))
    if res:
        res = res[0]
        json_data = json.dumps(res, ensure_ascii=False)

        return json_data
    return '无数据'

