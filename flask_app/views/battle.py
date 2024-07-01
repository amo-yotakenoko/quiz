from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db,socketio
from flask_socketio import SocketIO, send, emit ,join_room,leave_room, close_room, rooms, disconnect, ConnectionRefusedError
from flask_cors import CORS
import uuid

battle_module = Blueprint("battle", __name__)

rooms_data= {}
@battle_module.route('/battle', methods=['GET'])
def battle_get():
    room_id= rooms[0]
    return render_template('battle.html',room_id=1234,is_owner=False)


@battle_module.route("/rooms",methods=['GET'])
def rooms_get():
    return render_template('room_select.html',rooms_data=rooms_data)

@battle_module.route("/rooms/<id>",methods=['GET'])
def questions_get(id):
    return render_template('battle.html',room_id=id,is_owner=False)

#クライアントとのコネクション確立
# @socketio.on('connect')
# def connect():
#     emit('client_echo',{'msg': 'server connected!'})
#     socketio.emit('add_log', msg)

@battle_module.route('/room_create', methods=['GET'])
def room_create():
    room_id=uuid.uuid4()
    # room_id="1234"
    rooms_data[f"{room_id}"] = {"log": "", "members": []}
    socketio.start_background_task(battle_game,room_id)
    return render_template('battle.html',room_id=room_id,is_owner=True)


#クライアントからのメッセージを出力する関数
@socketio.on('join')
def join(msg):
    print( f"{msg}がjoin",flush=True)
    socketio.emit('add_log', { "text": f"{msg['username']}がjoin" })  
    #TODO:部屋を抜けたとき
    rooms_data[msg['room_id']]["members"].append(msg['username'])
    print(rooms_data[msg['room_id']],flush=True)
      

@socketio.on('message')
def message(msg):
    print(msg,flush=True)
    socketio.emit('add_log', msg)  



def battle_game(room_id):
    i=0
    while True:
        i+=1
        socketio.sleep(10) 
        socketio.emit('update_data', {'time': i})  
        print(rooms_data,flush=True)

