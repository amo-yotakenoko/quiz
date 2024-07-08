from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db,socketio
from flask_socketio import SocketIO, send, emit ,join_room,leave_room, close_room, rooms, disconnect, ConnectionRefusedError
from flask_cors import CORS
import uuid
# from flask import current_app
lobby_module = Blueprint("lobby", __name__)

rooms_data= {}
# @lobby_module.route('/battle', methods=['GET'])
# def battle_get():
#     room_id= rooms[0]
#     return render_template('lobby.html',room_id=1234,is_owner=False)


@lobby_module.route("/rooms",methods=['GET'])
def rooms_get():
    questions_sets = models.Questionset.query.all()
    return render_template('room_select.html',rooms_data=rooms_data,uuid=uuid.uuid4())

@lobby_module.route("/rooms/<id>",methods=['GET'])
def room_get(id):
    room_id=id
    is_owner=False
    if f"{room_id}" not in rooms_data:
        rooms_data[f"{room_id}"] = {"status": "waiting_to_join", "members": [],"question_set":[]}
        is_owner=True

    questions_sets = models.Questionset.query.all()
    return render_template('lobby.html',room_id=id,is_owner=is_owner,questions_sets= questions_sets)

#クライアントとのコネクション確立
# @socketio.on('connect')
# def connect():
#     emit('client_echo',{'msg': 'server connected!'})
#     socketio.emit('add_log', msg)

# @lobby_module.route('/room_create/', methods=['GET'])
# def room_create():
#     room_id=uuid.uuid4()
#     # room_id="1234"
#     rooms_data[f"{room_id}"] = {"status": "waiting_to_join", "members": []}
#     socketio.start_background_task(lobby_wait,f"{room_id}")
#     return render_template('lobby.html',room_id=room_id,is_owner=True)


#クライアントからのメッセージを出力する関数
@socketio.on('join')
def join(msg):
    room_id=msg['room_id']
    print( f"{msg}がjoin",flush=True)
    join_room(room_id)
    socketio.emit('add_log', { "text": f"{msg['username']}がjoin" } ,room=room_id)  
    #TODO:部屋を抜けたとき
    if msg['username'] not in rooms_data[room_id]["members"]:
        rooms_data[room_id]["members"].append(msg['username'])
    print(rooms_data[room_id],flush=True)
      

@socketio.on('message')
def message(msg):
    print(msg,flush=True)
    socketio.emit('add_log', msg,room=msg['room_id'])  

@socketio.on('select_questionset')
def select_questionset(msg):
    print(msg,flush=True)
    room_id=msg['room_id']
    question_set_id=msg["questionset"]
    enable=msg["enable"]
    print(question_set_id,enable,flush=True)
    if(enable):
        rooms_data[ room_id]["question_set"].append(question_set_id)
        socketio.emit('add_log',{ "text": f"{ models.Questionset.query.filter_by(questionsetid=question_set_id).first().questionsetitle}が追加" },room=msg['room_id'])  

    else:
        rooms_data[ room_id]["question_set"].remove(question_set_id)
        socketio.emit('add_log',{ "text": f"{ models.Questionset.query.filter_by(questionsetid=question_set_id).first().questionsetitle}が削除" },room=msg['room_id'])  
    # if()

    




# def lobby_wait(room_id):
#     while rooms_data[room_id]['status']=="waiting_to_join":
#         socketio.sleep(1)
#         # print(room_id,flush=True)
#         # socketio.emit('update_data', {'time': i})  
#         socketio.emit('add_log', {'text': f"{rooms_data[room_id]['status']}"},room=room_id)
#     socketio.emit('add_log', {'text': "ゲーム開始"} ,room=room_id)
#     socketio.sleep(1)
#     socketio.emit('redirect', {'url': f"battle/{room_id}"},room=room_id)

#         # quastions=[]
        # for username in rooms_data[room_id]["members"]:
        #         print(f" username{username}",flush=True)
        #         userid = models.Account.query.filter_by(name=username).one_or_none()
        #         print(f" userid{userid}",flush=True)
        #             # questionsetid = models.Questionset.query.filter_by(questionsetowner=userid).one_or_none().questionsetid
        #             # print(f" questionsetid{userid}",flush=True)
        #             # quastions.extend(models.Question.query.filter_by(questionsetid=questionsetid).questionid)
        # print(f"{quastions}",flush=True)
        # # socketio.emit('add_log', {'text': f"{quastions}"})

        # while True:
        #     i+=1
        #     socketio.sleep(10) 
        #     socketio.emit('update_data', {'time': i})  
        #     print(rooms_data,flush=True)
