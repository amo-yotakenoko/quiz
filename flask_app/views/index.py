from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user


index_module = Blueprint("index", __name__)



@index_module.route("/",methods=['GET'])
def index_get():
    print("index",flush=True)

    return render_template('index.html')

