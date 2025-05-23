import sqlite3
import os
from datetime import datetime


class SQLiteDB:
    def __init__(self, db_name='currency.db', db_dir='./data'):
        """
        初始化SQLite数据库连接
        :param db_name: 数据库文件名
        :param db_dir: 数据库存储目录
        """
        os.makedirs(db_dir, exist_ok=True)  # 创建存储目录（如果不存在）
        db_path = os.path.join(db_dir, db_name)  # 构建数据库路径
        # self.connection = sqlite3.connect(db_path)  # 连接数据库
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self, create_table_sql):
        """
        创建表
        :param create_table_sql: 创建表的SQL语句
        """
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
            print("表创建成功")
        except sqlite3.Error as e:
            print(f"创建表失败: {e}")

    def insert_data(self, insert_sql, data):
        """
        插入数据
        :param insert_sql: 插入数据的SQL语句
        :param data: 要插入的数据（单条或多条）
        """
        try:
            if isinstance(data, list):
                self.cursor.executemany(insert_sql, data)
            else:
                self.cursor.execute(insert_sql, data)
            self.connection.commit()
            print("数据插入成功")
        except sqlite3.Error as e:
            print(f"插入数据失败: {e}")

    def query_data(self, query_sql,data):
        """
        查询数据
        :param query_sql: 查询数据的SQL语句
        :return: 查询结果
        """
        try:
            self.cursor.execute(query_sql,data)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"查询数据失败: {e}")
            return []

    def update_data(self, update_sql, data):
        """
        更新数据
        :param update_sql: 更新数据的SQL语句
        :param data: 更新的数据
        """
        try:
            self.cursor.execute(update_sql, data)
            self.connection.commit()
            print("数据更新成功")
        except sqlite3.Error as e:
            print(f"更新数据失败: {e}")

    def delete_data(self, delete_sql, data=None):
        """
        删除数据
        :param delete_sql: 删除数据的SQL语句
        :param data: 删除条件的数据
        """
        try:
            if data:self.cursor.execute(delete_sql, data)
            else: self.cursor.execute(delete_sql)
        
            self.connection.commit()
            print("数据删除成功")
        except sqlite3.Error as e:
            print(f"删除数据失败: {e}")

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.connection.close()
        print("数据库连接已关闭")


# 示例使用
if __name__ == '__main__':
    db = SQLiteDB()

    # 创建表
    # create_table_sql = '''
    # CREATE TABLE IF NOT EXISTS currency (
    #     id INTEGER PRIMARY KEY,
    #     c_name TEXT NOT NULL,
    #     c_value DECIMAL(10, 4),
    #     date TEXT NOT NULL
    # )
    # '''
    # db.create_table(create_table_sql)
    # 获取当前日期和时间
    #current_datetime = datetime.now()
    # 格式化输出
    #formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # # 插入数据
    # db.insert_data("INSERT INTO currency (c_name, c_value, date) VALUES (?, ?, ?)", ('新西兰元', 4.2461, formatted_datetime))
  
    # # 查询数据
    # rows = db.query_data("SELECT * FROM currency")
    # print("查询结果:")
    # for row in rows:
    #     print(row)

    # # 更新数据
    # db.update_data("UPDATE users SET age = ? WHERE name = ?", (26, 'Alice'))

    # # 删除数据
    # db.delete_data("DELETE  FROM currency")

    # # 关闭连接
    db.close()
