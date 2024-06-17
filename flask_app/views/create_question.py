from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

create_question_module = Blueprint("create_question", __name__)


@create_question_module.route("/quastion/<id>",methods=['GET'])
def create_question_get(id):
    return render_template('create_question.html')

@create_question_module.route("/quastion/<id>",methods=['POST'])
def create_question_post(id):
    return render_template('create_question.html')