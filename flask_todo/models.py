from flask_todo import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

# 認証ユーザーの呼び出し方を定義
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Userテーブルの定義（UserMixinを継承してテーブルを定義）
class User(UserMixin, db.Model):
    # テーブル名
    __tablename__ = 'users'
    
    # カラム定義
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    
    # 各カラムを引数として使えるように設定
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
    
    # パスワード比較検証
    def validate_password(self, password):
        return check_password_hash(self.password, password)

    # emailで検索した時に一番最初にあるemailを取得（email は一意）  
    # True or False で返ってくる
    @classmethod
    def select_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
