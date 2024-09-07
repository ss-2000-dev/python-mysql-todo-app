import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'todo_app.login'
login_manager.login_message = 'ログインして下さい'

db = SQLAlchemy()
migrate = Migrate()

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
db_name = os.getenv('MYSQL_DB')

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'mysite'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{password}@{host}/{db_name}'
    # Trueにするとメモリを消費してしまうため、今回はFalse
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # views.pyに記述するBlueprintという機能を使用できるように設定
    from flask_todo.views import bp
    
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app
