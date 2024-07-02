from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db,socketio
from flask_socketio import SocketIO, send, emit ,join_room,leave_room, close_room, rooms, disconnect, ConnectionRefusedError
from flask_cors import CORS
import uuid
from flask_app.views.lobby import rooms_data

battle_module = Blueprint("battle", __name__)


@socketio.on('game_start')
def message(msg):
    print(msg,flush=True)
    room_id=msg['room_id']
    rooms_data[room_id]["status"]="in_progress"
    socketio.emit('add_log', {'text': "ゲーム開始"} ,room=room_id)
    socketio.sleep(1)
    socketio.emit('redirect', {'url': f"battle/{room_id}"},room=room_id)
    questions = quastions_get(room_id)
    print(questions,flush=True)
    socketio.sleep(1)
    socketio.emit('add_log', {'text': f"ゲーム開始"} ,room=room_id)
    for question in questions:
        socketio.sleep(1)
        print(f"問題:{question.questiontext}",flush=True)
        socketio.emit('add_log', {'text': f"問題:{question.questiontext}"} ,room=room_id)


@battle_module.route("/rooms/battle/<id>",methods=['GET'])
def battles_get(id):
    room_id=id
    return render_template('battle.html',room_id=room_id)


def quastions_get(room_id):
    questions = []
    for username in rooms_data[room_id]["members"]:
        user = models.Account.query.filter_by(name=username).first()
        if user:
            print(user.id,flush=True)
            questionsets = models.Questionset.query.filter_by(questionsetowner=user.id).all()
            for questionset in questionsets:
                print(questionset.questionsetid,flush=True)
                questions_in_set = models.Question.query.filter_by(questionsetid=questionset.questionsetid).all()
                for question in questions_in_set:
                    if(question not in questions):
                        questions.append(question)
                    print(question.questionid,flush=True)
    return questions
    print(questions,flush=True)
    