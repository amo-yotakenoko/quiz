from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from flask_app import models
from flask_app import db,socketio
from flask_socketio import SocketIO, send, emit ,join_room,leave_room, close_room, rooms, disconnect, ConnectionRefusedError
from flask_cors import CORS
import uuid
from flask_app.views.lobby import rooms_data
import random
import json
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
    rooms_data[room_id]["score"]={}
    for user in rooms_data[room_id]["members"]:
        rooms_data[room_id]["score"][user]=0
    update_ranking(room_id)
    for question in questions:
        print(f"問題:{question.questiontext}",flush=True)
        rooms_data[room_id]["questionid"]=question.questionid
        rooms_data[room_id]["correct_order"]=0
        # socketio.emit('add_log', {'text': f"問題:{question.questiontext}"} ,room=room_id)
        question_text = question.questiontext
        answer_correct = question.answer
        # 選択式問題なら選択肢も表示させる
        if question.questionformat == 1:
            answers_json = json.loads(question.answer)
            choices = [answers_json[key] for key in ["choice_correct", "choice_incorrect1", "choice_incorrect2", "choice_incorrect3"]]
            choice_map = [x for x in range(len(choices))]
            rooms_data[room_id]["choice_map"] = choice_map
            random.shuffle(choice_map)
            for i in range(len(choices)):
                choice = choice_map.index(i)
                question_text += "<br>{}. {}".format(i + 1, choices[choice])
            answer_correct = answers_json["choice_correct"]

        socketio.emit('question', question_text, room=room_id)
        for i in range(10,0,-1):
            socketio.emit('timer', i ,room=room_id)
            socketio.sleep(1)
        socketio.emit('add_log', {'text': f"答え:{answer_correct}"} ,room=room_id)
        socketio.sleep(1)
    socketio.emit('add_log', {'text': f"終わりです<a href=\"{ url_for('index.index_get') }\" >戻る</a>"} ,room=room_id)
    rooms_data[room_id]["status"]="finish"
    # socketio.emit('question',"おわり" ,room=room_id)
    print(url_for('lobby.room_get'),flush=True)


@socketio.on('send_answer')
def message(msg):
    print(msg,flush=True)
    room_id=msg['room_id']
    username=msg['username']
    question=models.Question.query.filter(models.Question.questionid ==  rooms_data[f"{room_id}"]["questionid"]).first()
    
    if question.questionformat == 0:
        is_correct=msg['answer']==question.answer
    else:
        correct_choice = rooms_data[room_id]["choice_map"][0] + 1
        is_correct = msg["answer"] == str(correct_choice)
    log='🙆‍♂️' if is_correct else '🙅'
    if( is_correct):
        rooms_data[room_id]["correct_order"]+=1
        addpoint=1
        if(rooms_data[room_id]["correct_order"]==1):
            addpoint=10
        if(rooms_data[room_id]["correct_order"]==2):
            addpoint=5
        if(rooms_data[room_id]["correct_order"]==3):
            addpoint=2
        rooms_data[room_id]["score"][username]+=addpoint
        update_ranking(room_id)
        log+=f"+{addpoint}points"
        # socketio.emit('correct', "正解" )  

    if(question.correctcount is None):
        question.correctcount=0
    if(question.count is None):
        question.count=0

    question.count+=1

    if(is_correct):
        question.correctcount+=1
    db.session.commit()

    # if(is_correct):
    #     msg['answer']="----"
    socketio.emit('post_answer', {'username':username,'answer':msg['answer'],'is_correct':is_correct},room=msg['room_id'])  

def update_ranking(room_id):
    ranking= dict(sorted( rooms_data[room_id]["score"].items(), key=lambda x: x[1], reverse=True))
    socketio.emit('update_ranking',ranking,room=room_id)  


@battle_module.route("/rooms/battle/<id>",methods=['GET'])
def battles_get(id):
    room_id=id
    return render_template('battle.html',room_id=room_id)


def quastions_get(room_id):
    questions = []
    for questionsetid in  rooms_data[room_id]["question_set"]:
        questions_set = models.Question.query.filter_by(questionsetid=questionsetid).all()
        for question in questions_set:
            if(question not in questions):
                questions.append(question)
            print(question.questionid,flush=True)
    random.shuffle(questions)
    # questions = questions[:10]
    return questions


# #ユーザーの奴全部とる奴、没
# def quastions_get(room_id):
#     questions = []
#     for username in rooms_data[room_id]["members"]:
#         user = models.Account.query.filter_by(name=username).first()
#         if user:
#             print(user.id,flush=True)
#             questionsets = models.Questionset.query.filter_by(questionsetowner=user.id).all()
#             for questionset in questionsets:
#                 print(questionset.questionsetid,flush=True)
#                 questions_in_set = models.Question.query.filter_by(questionsetid=questionset.questionsetid).all()
#                 for question in questions_in_set:
#                     if(question not in questions):
#                         questions.append(question)
#                     print(question.questionid,flush=True)
#     random.shuffle(questions)
#     # questions = questions[:10]
#     return questions