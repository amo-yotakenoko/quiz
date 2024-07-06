from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

create_question_module = Blueprint("create_question", __name__)


@create_question_module.route("/question/<id>",methods=['GET'])
def create_question_get(id):
    question = models.Question.query.filter_by(questionid=id).one_or_none()
    return render_template('create_question.html', id=id,question=  question)

@create_question_module.route("/question/<id>",methods=['POST'])
def create_question_post(id):
    print("問題が変更",flush=True)
    question = models.Question.query.filter_by(questionid=id).one_or_none()
    if question == None:
        return Response(response="<h1>404 Not found<h1/>create_question_module", status=404)
    question.questiontext=request.form["question"]
    question.answer=request.form["answer"]
    db.session.add(question)
    db.session.commit()
    print(question.questionsetid,flush=True)
    return redirect(url_for('questions_set.questions_get', id=question.questionsetid))