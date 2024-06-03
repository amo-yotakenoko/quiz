from database import db
from werkzeug.security import generate_password_hash, check_password_hash

# DBのテーブルを定義する
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # テーブル名を指定

    # 文字列型のnameカラム
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)

    mail = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
    def check_password(self, password):
            return check_password_hash(self.password, password)


