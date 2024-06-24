from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db
# import uuid
# from flask_app import app

# from main import login

# login = LoginManager(app)
# @login.user_loader
# def load_user(id):
#     # ログイン機能からidを受け取った際、DBからそのユーザ情報を検索し、返す
#     return models.User.query.get(int(id))

# login = LoginManager(app)

login_module = Blueprint("login", __name__)




# ログインページの実装
@login_module.route('/login', methods=['GET'])
def login_get():
  # 現在のユーザーがログイン済みの場合
  if current_user.is_authenticated:
    # トップページに移動
    return redirect(url_for('index.index_get'))
  
  # loginページのテンプレートを返す
  return render_template('login.html')


# メールアドレスとパスワードを受け取り処理を行う
@login_module.route('/login', methods=['POST'])
def login_post():
    # メールアドレスをもとにデータベースへ問い合わせる
    # 結果がゼロの時はNoneを返す
    user = models.Account.query.filter_by(name=request.form["userid"]).one_or_none()
    
    # ユーザが存在しない or パスワードが間違っている時
    if user is None or not user.check_password(request.form["password"]):
        # メッセージの表示
        flash('メールアドレスかパスワードが間違っています')
        # loginページへリダイレクト
        return redirect(url_for('login_get'))

    # ログインを承認
    login_user(user)
    # トップページへリダイレクト
    return redirect(url_for('index.index_get'))







# ログインページの実装
@login_module.route('/signup', methods=['GET'])
def register_get():
  # 現在のユーザーがログイン済みの場合
  if current_user.is_authenticated:
    # トップページに移動
    return redirect(url_for('index.index_get'))
  
  # loginページのテンプレートを返す
  return render_template('create_account.html')


# メールアドレスとパスワードを受け取り処理を行う
@login_module.route('/signup', methods=['POST'])
def register_post():
    user = models.Account(
        name=request.form["new_userid"],
        # id=str(uuid.uuid4())
    )
   
    user.set_password(request.form["new_password"])
    print("登録")
    # オブジェクトをDBに追加
    db.session.add(user)
    # DBへの変更を保存
    db.session.commit()
    return redirect(url_for('index.index_get'))


@login_module.route('/logout')
def logout():
    logout_user()

@login_module.route("/users",methods=['GET'])
def users_get():
    # ユーザオブジェクトを全て取得
    users = models.Account.query.all()
    return render_template('users_get.html', users=users)