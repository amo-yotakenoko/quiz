from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
import models 


app = Flask(__name__)


# DB_USER = "docker"
# DB_PASS = "docker"
# DB_HOST = "db"
# DB_NAME = "flask_app"
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"


app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///blog.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# セッション情報を暗号化するための秘密鍵（本番環境ではランダムかつ厳重に扱う）
app.secret_key = "secret"

# ログイン機能の有効化
login = LoginManager(app)

@login.user_loader
def load_user(id):
    # ログイン機能からidを受け取った際、DBからそのユーザ情報を検索し、返す
    return models.User.query.get(int(id))

migrate = Migrate(app)

db.init_app(app)




from login import login_module
app.register_blueprint(login_module)



@app.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)