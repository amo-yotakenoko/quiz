from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

quastions_module = Blueprint("quastions", __name__)



@quastions_module.route("/quastion/<id>",methods=['GET'])
def quastions_set_get():
    quastions = models.Question.query.all()
    return render_template('quastions.html',quastions_sets=  quastions)
