from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)


    app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///blog.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "secret"


    



    migrate = Migrate(app)

    # DBの設定
    db.init_app(app)
    from flask_app import models

    # Blueprintの登録
    from flask_app.views.index import index_module
    from flask_app.views.login import login_module
    app.register_blueprint(index_module)
    app.register_blueprint(login_module)

    return app

