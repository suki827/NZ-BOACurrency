
from app import create_app

# 创建 Flask 应用实例
app = create_app()

if __name__ == '__main__':
    # 运行 Flask 应用
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)

