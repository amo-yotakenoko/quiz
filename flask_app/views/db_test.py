from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

def insart_testdata():
    user1 = models.models.Questionset(questionsetitle="初級数学クイズ", questionsetowner=1)
    db.session.add(user1)
    db.session.commit()

    question1_user1 = models.Question(questionsetid=user1.questionsetid,
                                questiontext="2 + 2 = ?",
                                answer="4",
                                questionformat=1)
    db.session.add(question1_user1)

    question2_user1 = models.Question(questionsetid=user1.questionsetid,
                                questiontext="5 × 5 = ?",
                                answer="25",
                                questionformat=1)
    db.session.add(question2_user1)

    question3_user1 = models.Question(questionsetid=user1.questionsetid,
                                questiontext="10 ÷ 2 = ?",
                                answer="5",
                                questionformat=1)
    db.session.add(question3_user1)

    question4_user1 = models.Question(questionsetid=user1.questionsetid,
                                questiontext="3² = ?",
                                answer="9",
                                questionformat=1)
    db.session.add(question4_user1)

    question5_user1 = models.Question(questionsetid=user1.questionsetid,
                                questiontext="4 - 1 = ?",
                                answer="3",
                                questionformat=1)
    db.session.add(question5_user1)

    db.session.commit()

    # ユーザー2のクイズセットとクイズの作成
    user2 = models.models.Questionset(questionsetitle="動物の科学クイズ", questionsetowner=2)
    db.session.add(user2)
    db.session.commit()

    question1_user2 = models.Question(questionsetid=user2.questionsetid,
                                questiontext="カエルは両生類である。これは○か×か？",
                                answer="○",
                                questionformat=0)
    db.session.add(question1_user2)

    question2_user2 = models.Question(questionsetid=user2.questionsetid,
                                questiontext="最も速い陸上動物は何か？",
                                answer="チーター",
                                questionformat=0)
    db.session.add(question2_user2)

    question3_user2 = models.Question(questionsetid=user2.questionsetid,
                                questiontext="イヌ科の動物で最も大きなものは？",
                                answer="ライオン",
                                questionformat=0)
    db.session.add(question3_user2)

    question4_user2 = models.Question(questionsetid=user2.questionsetid,
                                questiontext="ペンギンのような鳥は何と呼ばれるか？",
                                answer="キングペンギン",
                                questionformat=0)
    db.session.add(question4_user2)

    question5_user2 = models.Question(questionsetid=user2.questionsetid,
                                questiontext="ゾウの鼻は何と呼ばれるか？",
                                answer="鼻先",
                                questionformat=0)
    db.session.add(question5_user2)

    db.session.commit()

    # ユーザー3のクイズセットとクイズの作成
    user3 = models.models.Questionset(questionsetitle="文学のクイズ", questionsetowner=3)
    db.session.add(user3)
    db.session.commit()

    question1_user3 = models.Question(questionsetid=user3.questionsetid,
                                questiontext="ウィリアム・シェイクスピアの劇作家としての最初の成功作は？",
                                answer="ロミオとジュリエット",
                                questionformat=0)
    db.session.add(question1_user3)

    question2_user3 = models.Question(questionsetid=user3.questionsetid,
                                questiontext="ジェーン・オースティンの小説「プライドと偏見」の主人公の名前は？",
                                answer="エリザベス・ベネット",
                                questionformat=0)
    db.session.add(question2_user3)

    question3_user3 = models.Question(questionsetid=user3.questionsetid,
                                questiontext="フランツ・カフカの小説「変身」の主人公が昆虫に変わる原因は？",
                                answer="不明",
                                questionformat=0)
    db.session.add(question3_user3)

    question4_user3 = models.Question(questionsetid=user3.questionsetid,
                                questiontext="ジョージ・オーウェルの小説「動物農場」で象徴される政治的制度は？",
                                answer="共産主義",
                                questionformat=0)
    db.session.add(question4_user3)

    question5_user3 = models.Question(questionsetid=user3.questionsetid,
                                questiontext="ロベルト・バウマンの小説「未来世界」で描かれるものは？",
                                answer="バーチャルリアリティ",
                                questionformat=0)
    db.session.add(question5_user3)

    db.session.commit()