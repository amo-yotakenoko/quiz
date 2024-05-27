from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint


login_module = Blueprint("login", __name__)




# ログインページの実装
@login_module.route('/login', methods=['GET'])
def login_get():
#   # 現在のユーザーがログイン済みの場合
#   if current_user.is_authenticated:
#     # トップページに移動
#     return redirect(url_for('index_get'))
  
#   # loginページのテンプレートを返す
  return render_template('login.html')


# # メールアドレスとパスワードを受け取り処理を行う
# @app.route('/login', methods=['POST'])
# def login_post():
#     # メールアドレスをもとにデータベースへ問い合わせる
#     # 結果がゼロの時はNoneを返す
#     user = User.query.filter_by(mail=request.form["mail"]).one_or_none()
    
#     # ユーザが存在しない or パスワードが間違っている時
#     if user is None or not user.check_password(request.form["password"]):
#         # メッセージの表示
#         flash('メールアドレスかパスワードが間違っています')
#         # loginページへリダイレクト
#         return redirect(url_for('login_get'))

#     # ログインを承認
#     login_user(user)
#     # トップページへリダイレクト
#     return redirect(url_for('index_get'))