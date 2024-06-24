from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

answer_quastion_module = Blueprint("answer_quastion", __name__)




@answer_quastion_module.route("/answer_quastion",methods=['GET'])
def answer_quastion_get(quastions):
    return render_template('answer_question.html',quastions=quastions)
