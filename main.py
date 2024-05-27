from flask import Flask, render_template, request, Response, redirect, url_for, flash



app = Flask(__name__)


from login import login_module
app.register_blueprint(login_module)




@app.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)