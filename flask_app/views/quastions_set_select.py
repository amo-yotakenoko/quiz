from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint, jsonify
from flask_app import models
from flask_app import db
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

quastions_set_select_module = Blueprint("quastions_set_select", __name__)


@quastions_set_select_module.route("/quastions_set_select",methods=['GET'])
def quastions_set_select_get():
    #TODO:所有者でフィルタする
    quastions_sets = models.Questionset.query.all()
    print('hello', flush=True)
    return render_template('quastions_set_select.html',quastions_sets= quastions_sets)



@quastions_set_select_module.route("/quastions_set_select",methods=['POST'])
def quastions_set_select_post():
    switchs = request.form.getlist("switch")
    # print(switchs,flush=True)
    return f"quastion{switchs}"
