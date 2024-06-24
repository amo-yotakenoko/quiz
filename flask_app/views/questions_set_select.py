from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

questions_set_select_module = Blueprint("questions_set_select", __name__)


@questions_set_select_module.route("/questions_set_select",methods=['GET'])
def questions_set_select_get():
    #TODO:所有者でフィルタする
    questions_sets = models.Questionset.query.all()
    return render_template('questions_set_select.html',questions_sets= questions_sets)



@questions_set_select_module.route("/questions_set_select",methods=['POST'])
def questions_set_select_post():
    switchs = request.form.getlist("switch")
    print(switchs,flush=True)
    questions=[]
    for questions_set_id in switchs:
        for question in models.Question.query.filter(models.Question.questionsetid == questions_set_id):
            questions.append(question)
        

    return render_template('answer_question.html',questions=questions)
