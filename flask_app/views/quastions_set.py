from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

quastions_set_module = Blueprint("quastions_set", __name__)



@quastions_set_module.route("/quastions_set",methods=['GET'])
def quastions_set_get():
    #TODO:所有者でフィルタする
    quastions_sets = models.Questionset.query.all()
    return render_template('quastions_set.html',quastions_sets= quastions_sets)

@quastions_set_module.route("/quastions_set",methods=['POST'])
def add_questionset():
    request_data = models.Questionset(questionsetitle ="",questionsetowner=current_user.get_id())
    db.session.add(request_data)
    db.session.commit()
    #TODO:ここ直接行けるようにしたい
    return redirect(url_for('quastions_set.add_questionset'))


@quastions_set_module.route("/quastions_set/<id>",methods=['GET'])
def quastions_get(id):
    quastions = models.Question.query.filter_by(questionsetid=id)
    # if  quastions == None:
    #     return Response(response="<h1>404 Not found<h1/>", status=404)
    return render_template('quastions.html',quastions=  quastions)


@quastions_set_module.route("/quastions_set/<id>",methods=['POST'])
def quastions_set(id):
    #TODO:問題タイプここで選ぶ?
    request_data = models.Question(questionsetid=id,questiontext="quiz")
    db.session.add(request_data)
    db.session.commit()
    #TODO:ここ直接行けるようにしたい
    return redirect(url_for('quastions_set.quastions_get', id=id))
