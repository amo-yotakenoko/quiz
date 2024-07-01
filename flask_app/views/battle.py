from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db
from flask_socketio import SocketIO, send, emit


battle_module = Blueprint("battle", __name__)

@battle_module.route('/battle', methods=['GET'])
def battle_get():
    return render_template('battle.html')