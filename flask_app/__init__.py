from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)


    app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///blog.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "secret"

    # DBの設定
    db.init_app(app)
    from flask_app import models
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    CORS(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return models.Account.query.filter_by(id=user_id).one_or_none()

    # Blueprintの登録
    from flask_app.views.index import index_module
    app.register_blueprint(index_module)
    from flask_app.views.login import login_module
    app.register_blueprint(login_module)
    from flask_app.views.questions_set import questions_set_module
    app.register_blueprint(questions_set_module)

    from flask_app.views.create_question import create_question_module 
    app.register_blueprint(create_question_module )
    from flask_app.views.questions_set_select import questions_set_select_module
    app.register_blueprint(questions_set_select_module)
    from flask_app.views.answer_question import answer_question_module
    app.register_blueprint(answer_question_module)
    from flask_app.views.battle import battle_module
    app.register_blueprint(battle_module)

    return app

