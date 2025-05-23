from flask import Flask



def create_app():
    app = Flask(__name__)
    # 导入配置
    app.config.from_object('app.config.Config')

    # 注册路由
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
