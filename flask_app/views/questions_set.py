from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

questions_set_module = Blueprint("questions_set", __name__)



@questions_set_module.route("/questions_set",methods=['GET'])
def questions_set_get():
   
    questions_sets = models.Questionset.query.filter_by(questionsetowner=current_user.get_id()).all()
    return render_template('questions_set.html',questions_sets= questions_sets)

@questions_set_module.route("/questions_set",methods=['POST'])
def add_questionset():
    request_data = models.Questionset(questionsetitle ="",questionsetowner=current_user.get_id())
    db.session.add(request_data)
    db.session.commit()

    return redirect(url_for('questions_set.questions_get',id=request_data.questionsetid))


@questions_set_module.route("/questions_set/<id>",methods=['GET'])
def questions_get(id):
    questions = models.Question.query.filter_by(questionsetid=id)
    questionsset = models.Questionset.query.filter_by(questionsetid=id).one_or_none()
    # if  questions == None:
    #     return Response(response="<h1>404 Not found<h1/>", status=404)
    return render_template('questions.html',questions=  questions,questionset=questionsset)


@questions_set_module.route("/questionsettitle_change",methods=['POST'])
def questionsettitle_change():
    print( request.json['questionsetid'],request.json['new_title'],flush=True)
    questionsset = models.Questionset.query.filter_by(questionsetid=request.json['questionsetid']).one_or_none()
    questionsset.questionsetitle=request.json['new_title']
    db.session.add(questionsset)
    db.session.commit()
    return "ok"

@questions_set_module.route("/questions_set/<id>",methods=['POST'])
def questions_set(id):

    request_data = models.Question(questionsetid=id,questiontext="quiz",count=0,correctcount=0)
    db.session.add(request_data)
    db.session.commit()

    return redirect(url_for('create_question.create_question_get', id=  request_data.questionid))
