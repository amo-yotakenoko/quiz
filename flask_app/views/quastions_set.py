from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

quastions_set_module = Blueprint("quastions_set", __name__)



@quastions_set_module.route("/quastions_set",methods=['GET'])
def quastions_set_get():
    quastions_sets = models.Questionset.query.all()
    return render_template('quastions_set.html',quastions_sets= quastions_sets)

@quastions_set_module.route("/quastions_set",methods=['POST'])
def add_questionset():
    request_data = models.Questionset(questionsetitle ="",questionsetowner=current_user.get_id())
    db.session.add(request_data)
    db.session.commit()
    #TODO:ここ直接行けるようにしたい
    return redirect(url_for('quastions_set.add_questionset'))

