from flask import Flask, render_template, request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text
import sqlite3 as sql

user_log=None

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Registration(db.Model):
    tablename = "registration"
    Username = db.Column(db.String(50),primary_key=True)
    Email = db.Column(db.String(50))
    Password = db.Column(db.String(50))

    def __init__(self, Username, Email, Password):
        self.Username = Username
        self.Email = Email
        self.Password = Password


class RegistrationSchema(ma.Schema):
    class Meta:
        fields = ("Username" , "Email", "Password")

registration_schema = RegistrationSchema()
registrations_schema = RegistrationSchema(many=True)

@app.route('/',methods=['GET','POST'])
def login():
    global user_log
    user_log = None
    return render_template("test.html")

@app.route('/success',methods=['POST','GET'])
def success():

    if request.method == 'POST':
        global user_log
        user = request.get_json()
        username = user[0]["username"]
        password = user[0]["password"]

        user_find = Registration.query.filter_by(Username=username).first()
        user_log = registration_schema.dump(user_find)
        if(len(user_log)>0):
            if (user_log['Username'] == username and user_log['Password'] == password):
                msg = {'message':"Successfully Login"}
            else:
                user_log = None
                msg = {'message':"Error: Incorrect Username or Password"}

        else:
            user_log = None
            msg = {'message':"Error: No User has been found"}
        return jsonify(msg)  
        
@app.route('/home',methods=['POST','GET'])
def home():
    global user_log
    if user_log is None:
        return redirect(url_for('login'))
    else:
        return render_template("home.html")
    
@app.route('/registration',methods=['POST'])
def registration():
    return render_template("reg.html")

@app.route('/doneregistration',methods=['POST','GET'])
def doneregistration():
    if request.method == 'POST':
        user = request.get_json()
        username = user[0]["username"]
        email = user[0]["email"]
        psw = user[0]["psw"]
        registered = Registration(username,email,psw)
        db.session.add(registered)
        db.session.commit()
        msg = {'message':"Successfully Registered"}

        return jsonify(msg)  
                #return redirect(url_for('registration'))
    #return render_template("reg.html",msg=msg)

@app.route('/list', methods=["GET"])
def list():
    global user_log
    if user_log is None:
        return redirect(url_for('login'))
    else:
        registration = Registration.query.all()
        result = registrations_schema.dump(registration)
        #print(result)
        return render_template('list.html', rows=result)


@app.route('/list/delete/<Username>',methods=['DELETE'])
def delete(Username):
    if request.method == 'DELETE':
        username = Registration.query.get(Username)
        db.session.delete(username)
        db.session.commit()
        registration = Registration.query.all()
        result = registrations_schema.dump(registration)
        print(result)
        return redirect(url_for('list'))
    return redirect(url_for('list'))

@app.route('/result',methods=['POST','GET'])
def result():

    global user_log
    if user_log is None:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            # do stuff when the form is submitted
            # redirect to end the POST handling
            # the redirect can be to the same route or somewhere else
            return redirect(url_for('home'))
        return render_template("info.html")

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0",port=8080, debug=True)