from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from db import *

app = Flask(__name__)

from login import login_module
app.register_blueprint(login_module)




@app.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)