from flask_app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# DBのテーブルを定義する
class Account(UserMixin, db.Model):
    # テーブル名を指定
    __tablename__ = 'Account'
    # 数値型のidカラム
    id = db.Column(db.String(128), primary_key=True)
    # 文字列型のnameカラム
    name = db.Column(db.String(128))

    # mail = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
    def check_password(self, password):
            return check_password_hash(self.password, password)


class Questionset(db.Model):

	__tablename__ = 'Questionset'
	# 数値型の問題セットIDカラム
	questionsetid = db.Column(db.Integer, primary_key=True,autoincrement=True)
	# 文字列型の問題セットタイトルカラム
	questionsetitle = db.Column(db.String(128))
	# 数値型の問題セット所有者カラム
	questionsetowner = db.Column(db.Integer)

class Question(db.Model):

	__tablename__ = 'Question'
    # 数値型の問題IDカラム
	questionid = db.Column(db.Integer, primary_key=True)
	# 文字列型の問題セットIDカラム
	questionsetid = db.Column(db.Integer)
	# 文字列型の問題文カラム
	questiontext = db.Column(db.String(128))
	# 文字列型の答えカラム
	answer = db.Column(db.String(128))
	# 数値型の問題の形式カラム(0:文字列問題,1:数値問題)
	questionformat = db.Column(db.Integer)
	# 数値型の問題が解かれた回数カラム
	count = db.Column(db.Integer)
	# 数値型の正解した回数カラム
	correctcount = db.Column(db.Integer)

class GameLog(db.Model):

	__tablename__ = 'GameLog'
    # 数値型のゲームログのIDカラム
	gamelogid = db.Column(db.Integer, primary_key=True)
	# 数値型の参加したユーザのIDカラム
	participatingiserid = db.Column(db.Integer)
	# 数値型のゲーム番号カラム
	gamenumber = db.Column(db.Integer)
	# 文字列型の問題セット一覧カラム
	questionsetlist = db.Column(db.String(128))
	# 数値型の出題された問題カラム
	questionasked = db.Column(db.Integer)
	# 文字列型のどのユーザがどう回答したかカラム
	howtoanswer = db.Column(db.String(128))


