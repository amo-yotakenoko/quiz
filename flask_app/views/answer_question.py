from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

answer_question_module = Blueprint("answer_question", __name__)




@answer_question_module.route("/answer_question",methods=['GET'])
def answer_question_get(questions):
    return render_template('answer_question.html',questions=questions)
