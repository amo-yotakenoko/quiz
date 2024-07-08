from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
import json
create_question_module = Blueprint("create_question", __name__)


@create_question_module.route("/question/<id>",methods=['GET'])
def create_question_get(id):
    question = models.Question.query.filter_by(questionid=id).one_or_none()
    selection =None
    if(question.questionformat==1):
        selection = json.loads(question.answer)

    return render_template('create_question.html', id=id,question=  question,selection=selection)

@create_question_module.route("/question_delete",methods=['POST'])
def question_delete():
    print( request.json['questionid'],"削除",flush=True)
    question = models.Question.query.filter_by(questionid=request.json['questionid']).one_or_none()

    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('questions_set.questions_get', id=question.questionsetid))

@create_question_module.route("/question/<id>",methods=['POST'])
def create_question_post(id):
    print("問題が変更",flush=True)
    question = models.Question.query.filter_by(questionid=id).one_or_none()
    if question == None:
        return Response(response="<h1>404 Not found<h1/>create_question_module", status=404)
    question.questiontext=request.form["question"]
    print(request.form.get("type"),flush=True)
    if(request.form.get("type")=="text"):
        question.questionformat=0
        question.answer=request.form["answer"]
    if(request.form.get("type")=="choice"):
        question.questionformat=1
        question.answer=json.dumps({"choice_correct":request.form["choice_correct"],
                                    "choice_incorrect1":request.form["choice_incorrect1"],
                                    "choice_incorrect2":request.form["choice_incorrect2"],
                                    "choice_incorrect3":request.form["choice_incorrect2"]})
        
    print(question.answer,flush=True)
    db.session.add(question)
    db.session.commit()
    print(question.questionsetid,flush=True)
    return redirect(url_for('questions_set.questions_get', id=question.questionsetid))