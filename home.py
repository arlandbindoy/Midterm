from flask import Flask, render_template, request,redirect,url_for
import sqlite3 as sql


app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('login'))

    # show the form, it wasn't submitted
    return render_template("test.html")

@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        print("login")
        username = request.form['username']
        password = request.form['password']
        con =sql.connect("database.db")
        con.row_factory =sql.Row
        cur=con.cursor()
        cur.execute(f"SELECT username from registration WHERE username='{username}' AND password = '{password}';")
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
            return redirect(url_for('login'))

        else:
            print("Welcome")
            return redirect(url_for('home'))
    return render_template("home.html")
@app.route('/registration',methods=['POST'])
def registration():
    return render_template("reg.html")

@app.route('/doneregistration',methods=['POST','GET'])
def doneregistration():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        try:
          username = request.form['username']
          email = request.form['email']
          psw = request.form['psw']
          with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO registration(Username,Email,Password) VALUES (?,?,?)",(username,email,psw))
                con.commit()
                msg="Successfully Registered"
          print('try')
        except:
            con.rollback()
            msg="Error Username Already taken"
            print('except')
        finally:
            print('finally')
            con.close()
            return render_template("result.html",msg=msg)  
                #return redirect(url_for('registration'))
    #return render_template("reg.html",msg=msg)

@app.route('/list', methods=["GET","POST"])
def list():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    con =sql.connect("database.db")
    con.row_factory =sql.Row
    cur=con.cursor()
    cur.execute("select * from registration")
    rows=cur.fetchall()
    print(rows)
    return render_template("list.html",rows=rows)

@app.route('/list/delete',methods=['POST'])
def delete():
    delete = request.form['delete']
    con =sql.connect("database.db")
    cur=con.cursor()
    cur.execute("delete from registration where Username='{}'".format(delete))
    con.commit()
    msg="Account Deleted Successfuly"
    return render_template("list2.html",msg=msg)

    

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    return render_template("info.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)