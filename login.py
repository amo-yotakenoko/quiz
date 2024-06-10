from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
import models 
from database import db


# from main import login




login_module = Blueprint("login", __name__)




# ログインページの実装
@login_module.route('/login', methods=['GET'])
def login_get():
  # 現在のユーザーがログイン済みの場合
  if current_user.is_authenticated:
    # トップページに移動
    return redirect(url_for('index_get'))
  
  # loginページのテンプレートを返す
  return render_template('LoginPage.html')


# メールアドレスとパスワードを受け取り処理を行う
@login_module.route('/login', methods=['POST'])
def login_post():
    # メールアドレスをもとにデータベースへ問い合わせる
    # 結果がゼロの時はNoneを返す
    user = models.User.query.filter_by(mail=request.form["userid"]).one_or_none()
    
    # ユーザが存在しない or パスワードが間違っている時
    if user is None or not user.check_password(request.form["password"]):
        # メッセージの表示
        flash('メールアドレスかパスワードが間違っています')
        # loginページへリダイレクト
        return redirect(url_for('login_get'))

    # ログインを承認
    login_user(user)
    # トップページへリダイレクト
    return redirect(url_for('index_get'))







# ログインページの実装
@login_module.route('/signup', methods=['GET'])
def register_get():
  # 現在のユーザーがログイン済みの場合
  if current_user.is_authenticated:
    # トップページに移動
    return redirect(url_for('index_get'))
  
  # loginページのテンプレートを返す
  return render_template('SignupPage.html')


# メールアドレスとパスワードを受け取り処理を行う
@login_module.route('/signup', methods=['POST'])
def register_post():
    user = models.User(
        name=request.form["new_userid"]
    )
   
    user.set_password(request.form["new_password"])
    print("登録")
    # オブジェクトをDBに追加
    db.session.add(user)
    # DBへの変更を保存
    db.session.commit()
    return redirect(url_for('index_get'))


@login_module.route("/users",methods=['GET'])
def users_get():
    # ユーザオブジェクトを全て取得
    users = models.User.query.all()
    return render_template('users_get.html', users=users)