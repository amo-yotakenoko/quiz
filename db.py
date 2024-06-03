from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash



class DB():

        
    



    # SQLAlchrmyの設定を記述する。composeファイルの環境変数で指定したとおり、データベース名や接続情報を指定する。
    DB_USER = "docker"
    DB_PASS = "docker"
    DB_HOST = "db"
    DB_NAME = "flask_app"
    db = None
    migrate = None

    def __init__(self,app):
        global DB_USER,DB_PASS,DB_HOST,DB_NAME
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


        # セッション情報を暗号化するために指定（※この値が漏洩するとログイン機能は全部突破されるため、本番環境ではランダムかつ厳重に扱う）
        app.secret_key = "secret"

        # ログイン機能の有効化
        login = LoginManager(app)

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)


        # DBのテーブルを定義する
        class User(db.Model):
            __tablename__=None
            id=None
            name=None
            age=None
            def __init__(self):
                # テーブル名を指定
                __tablename__ = 'Users'
                # 数値型のidカラム
                id = db.Column(db.Integer, primary_key=True)
                # 文字列型のnameカラム
                name = db.Column(db.String(128))
                age = db.Column(db.Integer)