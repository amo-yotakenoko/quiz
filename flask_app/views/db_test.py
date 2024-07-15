from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db
from flask_app.models import db, Questionset, Question

db_test_module = Blueprint("db_test", __name__)
@db_test_module.route('/add_test_quastion', methods=['GET'])
def insart_testdata():

    user1 = Questionset(questionsetitle="ChatGPTに作らせた初級数学クイズ", questionsetowner=0)
    db.session.add(user1)
    db.session.commit()

    question1_user1 = Question(questionsetid=user1.questionsetid,
                               questiontext="2 + 2 = ?",
                               answer="4",
                               questionformat=0)
    db.session.add(question1_user1)

    question2_user1 = Question(questionsetid=user1.questionsetid,
                               questiontext="5 × 5 = ?",
                               answer="25",
                               questionformat=0)
    db.session.add(question2_user1)

    question3_user1 = Question(questionsetid=user1.questionsetid,
                               questiontext="10 ÷ 2 = ?",
                               answer="5",
                               questionformat=0)
    db.session.add(question3_user1)

    question4_user1 = Question(questionsetid=user1.questionsetid,
                               questiontext="3² = ?",
                               answer="9",
                               questionformat=0)
    db.session.add(question4_user1)

    question5_user1 = Question(questionsetid=user1.questionsetid,
                               questiontext="4 - 1 = ?",
                               answer="3",
                               questionformat=0)
    db.session.add(question5_user1)

    db.session.commit()
    user1_2 = Questionset(questionsetitle="ChatGPTに作らせたPythonの基本クイズ", questionsetowner=0)
    db.session.add(user1_2)
    db.session.commit()

    question1_user1_2 = Question(questionsetid=user1_2.questionsetid,
                            questiontext="Pythonのコメントを記述する記号は何か？",
                            answer="#",
                            questionformat=0)
    db.session.add(question1_user1_2)

    question2_user1_2 = Question(questionsetid=user1_2.questionsetid,
                            questiontext="Pythonで文字列を結合する演算子は何か？",
                            answer="+",
                            questionformat=0)
    db.session.add(question2_user1_2)

    question3_user1_2 = Question(questionsetid=user1_2.questionsetid,
                            questiontext="Pythonで変数を代入する演算子は何か？",
                            answer="=",
                            questionformat=0)
    db.session.add(question3_user1_2)

    question4_user1_2 = Question(questionsetid=user1_2.questionsetid,
                            questiontext="Pythonで条件分岐を行うためのキーワードは何か？",
                            answer="if",
                            questionformat=0)
    db.session.add(question4_user1_2)

    question5_user1_2 = Question(questionsetid=user1_2.questionsetid,
                            questiontext="Pythonのリスト内包表記の記法はどうなっているか？",
                            answer="[式 for 要素 in イテラブル]",
                            questionformat=0)
    db.session.add(question5_user1_2)

    # ユーザー2のクイズセットとクイズの作成
    user2 = Questionset(questionsetitle="ChatGPTに作らせた動物の科学クイズ", questionsetowner=0)
    db.session.add(user2)
    db.session.commit()

    question1_user2 = Question(questionsetid=user2.questionsetid,
                               questiontext="カエルは両生類である。これは○か×か？",
                               answer="○",
                               questionformat=0)
    db.session.add(question1_user2)

    question2_user2 = Question(questionsetid=user2.questionsetid,
                               questiontext="最も速い陸上動物は何か？",
                               answer="チーター",
                               questionformat=0)
    db.session.add(question2_user2)

    question3_user2 = Question(questionsetid=user2.questionsetid,
                               questiontext="イヌ科の動物で最も大きなものは？",
                               answer="ライオン",
                               questionformat=0)
    db.session.add(question3_user2)

    question4_user2 = Question(questionsetid=user2.questionsetid,
                               questiontext="ペンギンのような鳥は何と呼ばれるか？",
                               answer="キングペンギン",
                               questionformat=0)
    db.session.add(question4_user2)

    question5_user2 = Question(questionsetid=user2.questionsetid,
                               questiontext="ゾウの鼻は何と呼ばれるか？",
                               answer="鼻先",
                               questionformat=0)
    db.session.add(question5_user2)

    db.session.commit()

    # ユーザー3のクイズセットとクイズの作成
    user3 = Questionset(questionsetitle="ChatGPTに作らせた文学のクイズ", questionsetowner=0)
    db.session.add(user3)
    db.session.commit()

    question1_user3 = Question(questionsetid=user3.questionsetid,
                               questiontext="ウィリアム・シェイクスピアの劇作家としての最初の成功作は？",
                               answer="ロミオとジュリエット",
                               questionformat=0)
    db.session.add(question1_user3)

    question2_user3 = Question(questionsetid=user3.questionsetid,
                               questiontext="ジェーン・オースティンの小説「プライドと偏見」の主人公の名前は？",
                               answer="エリザベス・ベネット",
                               questionformat=0)
    db.session.add(question2_user3)

    question3_user3 = Question(questionsetid=user3.questionsetid,
                               questiontext="フランツ・カフカの小説「変身」の主人公が昆虫に変わる原因は？",
                               answer="不明",
                               questionformat=0)
    db.session.add(question3_user3)

    question4_user3 = Question(questionsetid=user3.questionsetid,
                               questiontext="ジョージ・オーウェルの小説「動物農場」で象徴される政治的制度は？",
                               answer="共産主義",
                               questionformat=0)
    db.session.add(question4_user3)

    question5_user3 = Question(questionsetid=user3.questionsetid,
                               questiontext="ロベルト・バウマンの小説「未来世界」で描かれるものは？",
                               answer="バーチャルリアリティ",
                               questionformat=0)
    db.session.add(question5_user3)

    db.session.commit()
    return "追加しました"

@db_test_module.route('/delete_quiz', methods=['GET'])
def delete_quiz():
    db.session.query(models.Questionset).delete()
    db.session.query(models.Question).delete()
    db.session.commit()
    return "aa"
@db_test_module.route('/delete_users', methods=['GET'])
def delete_users():
    db.session.query(models.Account).delete()
    db.session.commit()
    return "aa"