from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import Blueprint



index_module = Blueprint("index", __name__)



@index_module.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')

